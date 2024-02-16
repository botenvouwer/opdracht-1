import os
from pathlib import Path

home_folder = Path(os.path.expanduser('~'))

FOLDER_PATH = home_folder / 'Downloads'
CSV_file_name = 'Cinecenter-product-sales.csv'
Excel_file_name = 'MSP.xlsx'
Test_excel_file_name = 'TestExcel.xlsx'
Test_csv_file_name = 'TestCSV.csv'
EMRE_TEST_CSV = 'input.csv'

DB_PARAMS = {
    'host': 'localhost',
    'port': '5432',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres'
}

EXCEL_PATH = FOLDER_PATH / Excel_file_name
CSV_PATH = FOLDER_PATH / CSV_file_name
TEST_CSV_PATH = FOLDER_PATH / Test_csv_file_name
TEST_EXCEL_PATH = FOLDER_PATH / Test_excel_file_name
# CSV_PATH = TEST_CSV_PATH
# TEST = FOLDER_PATH / CSV_file_name
EMRE_PATH = FOLDER_PATH / EMRE_TEST_CSV