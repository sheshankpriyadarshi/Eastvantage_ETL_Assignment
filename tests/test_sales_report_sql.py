import pandas as pd
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sql_soln.sales_report_sql import main as generate_sql_report

# Expected output columns
EXPECTED_COLUMNS = ["Customer", "Age", "Item", "Quantity"]
OUTPUT_PATH = "sql_soln/sql_result.csv"

@pytest.fixture
def run_sql_report():
    """Fixture to generate the report using the SQL script."""
    generate_sql_report()
    assert os.path.exists(OUTPUT_PATH), "Output CSV file was not created."
    return pd.read_csv(OUTPUT_PATH, delimiter=";")

def test_output_file_exists(run_sql_report):
    """Test that the output file is created."""
    assert os.path.exists(OUTPUT_PATH), "Output file not found!"

def test_output_file_structure(run_sql_report):
    """Test that the output file has the expected columns."""
    df = run_sql_report
    assert list(df.columns) == EXPECTED_COLUMNS, "Output columns do not match expected structure."

def test_non_empty_output(run_sql_report):
    """Test that the output file is not empty."""
    df = run_sql_report
    assert not df.empty, "Output file is empty."

def test_data_content(run_sql_report):
    """Testing the specific expected value matches."""
    df = run_sql_report
    assert df["Customer"].iloc[0] == 5, "First row value does not match expected."
