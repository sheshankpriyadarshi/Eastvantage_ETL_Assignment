import pandas as pd
from sqlalchemy import create_engine

try:
    # Set up the SQLite database connection 
    engine = create_engine('sqlite:///../DB/S30 ETL Assignment.db') 

    # Load tables into DataFrames
    customers_df = pd.read_sql_table("customers", engine)
    sales_df = pd.read_sql_table("sales", engine)
    orders_df = pd.read_sql_table("orders", engine)
    items_df = pd.read_sql_table("items", engine)

    # Merge DataFrames to combine relevant information
    merged_df = (
        orders_df
        .merge(sales_df, on="sales_id")
        .merge(customers_df, on="customer_id")
        .merge(items_df, on="item_id")
    )

    # Filter for customers aged 18-35 and non-null quantities
    filtered_df = merged_df[(merged_df["age"].between(18, 35)) & (merged_df["quantity"].notnull())]

    # Group by customer, age, and item, summing quantities
    result_df = (
        filtered_df
        .groupby(["customer_id", "age", "item_name"], as_index=False)
        .agg({"quantity": "sum"})
    )

    # Filter out zero quantities
    result_df = result_df[result_df["quantity"] > 0]

    # Convering the age and quantity column values to integer type
    result_df['age'] = result_df['age'].astype(int)
    result_df['quantity'] = result_df['quantity'].astype(int)

    # Rename columns to match output format
    result_df.columns = ["Customer", "Age", "Item", "Quantity"]

    # Write the result to CSV with ';' as delimiter
    result_df.to_csv("output_pandas_sqlalchemy.csv", sep=";", index=False)
except Exception as err:
    print(f'Error --- {err}')
finally: 
    engine.dispose()
