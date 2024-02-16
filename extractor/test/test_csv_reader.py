import unittest

from extractor.csv_reader import CSVReader
from model.entity import Header

TEST_CSV_PATH = "data/test.csv"


class TestCSVReader(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.csv_reader = CSVReader(TEST_CSV_PATH)

    def test_csv_name(self):
        csv = self.csv_reader
        self.assertEqual(csv.get_name(), 'test')
        csv.set_name('Foo#Bar')
        self.assertEqual(csv.get_name(), 'foo_bar')

    def test_delimiter(self):
        csv = self.csv_reader
        self.assertEqual(csv.delimiter_sniffer(), ';')
        self.assertNotEqual(csv.delimiter_sniffer(), '')
        self.assertIsInstance(csv.delimiter_sniffer(), str)
        self.assertEqual(len(csv.delimiter_sniffer()), 1)

    def test_get_header_names(self):
        csv = self.csv_reader
        self.assertEqual(csv.get_header_names(), ['foo', 'bar'])
        self.assertIsInstance(csv.get_header_names(), list)  # Ensure the returned value is a list
        self.assertNotEqual(csv.get_header_names(), [])  # Ensure the returned list is not empty
        self.assertNotEqual(csv.get_header_names(), ['test', 'test'])  # Ensure it's not equal to a specific dummy value

    def test_get_header_info(self):
        csv = self.csv_reader
        header_info = csv.get_header_info()
        self.assertIsInstance(header_info, list)  # Ensure the returned value is a list
        self.assertNotEqual(header_info, [])  # Ensure the returned list is not empty
        self.assertNotEqual(header_info, ['test', 'test'])  # Ensure it's not equal to a specific dummy value
        self.assertEqual(header_info, [x for x in header_info])  # Ensure the list is equal to itself
        self.assertEqual(len(csv.get_header_info()), 2)
        self.assertEqual(header_info[0].name, 'foo')
        self.assertEqual(header_info[0].datatype, 'TEXT')
        self.assertEqual(header_info[1].name, 'bar')
        self.assertEqual(header_info[1].datatype, 'INTEGER')




