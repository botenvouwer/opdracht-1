import unittest

from extractor.main import csv
from loader.postgres_loader import PostgresLoader

TEST_EXCEL_PATH = "/Users/olivier/Downloads/TestExcel.xlsx"


class TestPostgresLoader(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.postgres_loader = PostgresLoader(TEST_EXCEL_PATH)

    def test_number_of_sheets(self):
        loader = self.postgres_loader
        self.assertEqual(loader.define_drop_if_exists_sql('test'), "DROP TABLE IF EXISTS test")
        self.assertEqual(loader.define_drop_if_exists_sql(123), "DROP TABLE IF EXISTS 123")
        self.assertIsInstance(loader.define_drop_if_exists_sql('test'), str)


    def test_define_create_table(self):
        loader = self.postgres_loader
        define_create = loader.define_drop_if_exists_sql(TEST_EXCEL_PATH)
        self.assertIsInstance(define_create, str)
        self.assertEqual(define_create, "DROP TABLE IF EXISTS /Users/olivier/Downloads/TestExcel.xlsx")
        self.assertNotEqual(define_create, "")
        self.assertEqual(len(define_create), 60)

    def test_define_column_info(self):
        loader = self.postgres_loader
        header_list = csv.get_header_info()
        define_column = loader.define_column_info(header_list)
        self.assertIsInstance(define_column, str)
        self.assertEqual(define_column, "naam TEXT, salaris INTEGER, functie TEXT, geboren TEXT")
        self.assertNotEqual(define_column, "")
        self.assertEqual(len(define_column), 54)


    def test_define_insert_sql(self):
        loader = self.postgres_loader
        header_list = csv.get_header_info()
        define_insert = loader.define_insert_sql('test_2',header_list,'bla')
        self.assertEqual(define_insert, 'INSERT INTO test_2 (naam, salaris, functie, geboren) VALUES (%s, %s, %s);')
        self.assertIsInstance(define_insert, str)
        self.assertNotEqual(define_insert, "")


