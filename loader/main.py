from constants import CSV_PATH, TEST_EXCEL_PATH, EXCEL_PATH, TEST_CSV_PATH, DB_PARAMS, EMRE_PATH
from extractor.csv_reader import CSVReader
from extractor.excel_reader import ExcelReader
from extractor.reader import Reader

from loader.postgres_loader import PostgresLoader

excel = ExcelReader(TEST_EXCEL_PATH)
excel_2 = ExcelReader(EXCEL_PATH)
csv = CSVReader(TEST_CSV_PATH)
csv_2 = CSVReader(CSV_PATH)
csv_3 = CSVReader(EMRE_PATH)

reader: Reader = excel
header_list = csv.get_header_info()

loader = PostgresLoader(DB_PARAMS)
define_column = loader.define_column_info(header_list)
print(define_column)
