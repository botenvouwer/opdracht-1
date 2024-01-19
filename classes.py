from abc import ABC
from pathlib import Path


class DatasourceReader(ABC):

    def get_headers(self) -> list[(str, str)]:
        pass


class CSVDatasourceReader(DatasourceReader):

    def specificly_for_csv(self):
        pass

    def __init__(self, file_location: str):
        self.file_location = Path(file_location)

    def __str__(self):
        return f"CSVReader(file_location={self.file_location}, test={self.test})"


class ExcelDatasourceReader(DatasourceReader):

    def __init__(self, file_location: str):
        self.file_location = Path(file_location)

    def __str__(self):
        return f"CSVReader(file_location={self.file_location}, test={self.test})"


reader: DatasourceReader = CSVDatasourceReader("test.csv")
reader2: DatasourceReader = ExcelDatasourceReader("test.csv")

print(reader.get_headers())
print(reader2.get_headers())
