import extractor.excel_reader
from constants import TEST_EXCEL_PATH, TEST_CSV_PATH, CSV_PATH, DB_PARAMS, EXCEL_PATH
from extractor.csv_reader import CSVReader
from loader import postgres_loader


excel = extractor.excel_reader.ExcelReader(TEST_EXCEL_PATH)
excel_2 = extractor.excel_reader.ExcelReader(EXCEL_PATH)
csv = CSVReader(TEST_CSV_PATH)
csv_2 = CSVReader(CSV_PATH)
loader = postgres_loader.PostgresLoader(DB_PARAMS)

# excel.set_sheet_index(1)
# loader.load(excel_2)

# emre = CSVReader(EMRE_PATH)
# loader.load(emre)

# sniff = data_sniffer.DataSniffer('')
# print(sniff.get_type())
