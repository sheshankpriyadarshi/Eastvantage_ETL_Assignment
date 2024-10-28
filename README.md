# Eastvantage_ETL_Assignment
Sales report assignment using python, pandas & sql.

## Getting Started

This project aims to generate sales reports using data from a single database. It reads data from different tables within the database and compiles them into a CSV file format.

## Project Structure

```
.
├── DB
│   └── S30 ETL Assignment.db
├── pandas_soln
│   ├── sales_report_pandas.py
│   └── output_pandas_sqlalchemy.csv
├── sql_soln
│   ├── sales_report_sql.py
│   └── sql_result.csv
├── tests
│   ├── test_sales_report_pandas.py  # Unit test for Pandas solution
│   └── test_sales_report_sql.py     # Unit test for SQL solution
└── requirements.txt
```

## Installation Steps

1. Clone the repository:
    ```
    git clone https://github.com/sheshankpriyadarshi/Eastvantage_ETL_Assignment.git
    ```

2. Create a virtual environment and activate it:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

## Testing

```
pytest tests/
```

__NOTE:__ The below python files expects the database file to be in working directory(directory in which python files are present) -
          1. pandas_soln/sales_report_pandas.py
          2. sql_soln/sales_report_sql.py

__Prerequisite:__ The python files above have dependencies on other libraries such as pandas, sqlalchemy, etc. So, run the below pip command to install the dependencies using requirements.txt file before running the pyhton files - **pip install -r requirements.txt**
