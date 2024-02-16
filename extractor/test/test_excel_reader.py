import unittest

from extractor.excel_reader import ExcelReader

TEST_EXCEL_PATH = "/Users/olivier/Downloads/TestExcel.xlsx"


class TestCSVReader(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.excel_reader = ExcelReader(TEST_EXCEL_PATH)

    def test_csv_name(self):
        excel = self.excel_reader
        self.assertEqual(excel.get_name(), 'testexcel_0')
        excel.set_name('Foo#Bar')
        self.assertEqual(excel.get_name(), 'foo_bar_0')
        # excel.set_sheet_index(1)
        # self.assertEqual(excel.get_name(), 'foo_bar_1')

    def test_number_of_sheets(self):
        excel = self.excel_reader
        self.assertEqual(excel.get_number_of_sheets(), 2)

    def test_header_recoded(self):
        excel = self.excel_reader
        self.assertEqual(excel.header_info_recoded('n', 's'), 'TEXT')
        self.assertEqual(excel.header_info_recoded(54, 'n'), 'INTEGER')
        self.assertEqual(excel.header_info_recoded('', 's'), 'TEXT')
        self.assertIsInstance(excel.header_info_recoded('n','s'), str)
        self.assertIsInstance(excel.header_info_recoded('','s'), str)