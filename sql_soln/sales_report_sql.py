import sqlite3 as sql_engine
import sys
import csv


def main():
    conn_obj = "" 

    try: 
        # Establishing connection with database
        conn_obj = sql_engine.connect(r'DB/S30 ETL Assignment.db')
        # Initializing cursor object to execute SQL queries 
        cur = conn_obj.cursor()

        query = """
            SELECT 
                customers.customer_id AS Customer,
                customers.age AS Age,
                Items.item_name AS Item,
                SUM(Orders.quantity) AS Quantity
            FROM 
                customers
            JOIN 
                Sales ON customers.customer_id = Sales.customer_id
            JOIN 
                Orders ON Sales.sales_id = Orders.sales_id
            JOIN 
                Items ON Orders.item_id = Items.item_id
            WHERE 
                customers.age BETWEEN 18 AND 35
                AND Orders.quantity IS NOT NULL
            GROUP BY 
                customers.customer_id, Items.item_id
            HAVING 
                SUM(Orders.quantity) > 0
            ORDER BY 
                customers.customer_id, Items.item_name;
        """
        
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()
        print("Tables in the database:", tables)     

        customer_age_table = cur.execute(query)
        # Fetch all rows
        rows = cur.fetchall()

        csv_file_path = 'sql_result.csv'

        # Write the fetched rows to a CSV file with ';' as the delimiter
        with open(csv_file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=';')
            # Write the header
            csv_writer.writerow(['Customer', 'Age', 'Item', 'Quantity'])
            # Write the rows
            csv_writer.writerows(rows)
    except Exception as err: 
        if conn_obj: 
            conn_obj.rollback()
        print(f'Error --- {err}')
        sys.exit(1) 
    finally: 
        if conn_obj: 
            conn_obj.close()

if __name__ == "__main__":
    main()
