import csv

from extractor.data_sniffer import DataSniffer
from extractor.reader import Reader
from model.entity import Header


class CSVReader(Reader):
    def __init__(self, file_path):
        self.__name = None
        super().__init__(file_path)
        self.delimiter = self.delimiter_sniffer() or ';'

    def __iter__(self):
        with open(self.file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            next(csv_reader)

            for row in csv_reader:
                yield row

    def __str__(self):
        return f"CSV met volgende headers = {self.get_header_names()}"

    def delimiter_sniffer(self):  # naar data_sniffer verplaatsen?
        delimiters = [',', ';', '\t']  # common delimiters to check

        with open(self.file_path, 'r', newline='') as csvfile:
            # Read the first few lines to detect the delimiter
            for line in csvfile:
                for delimiter in delimiters:
                    if delimiter in line:
                        return delimiter

        # If none of the common delimiters are found, return None
        return None

    def get_header_info(self) -> [Header]:
        with open(self.file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            csv_headers = next(csv_reader)
            csv_first_record = next(csv_reader)

            csv_header_info = []
            for i, csv_header in enumerate(csv_headers):
                value = csv_first_record[i]

                sniff = DataSniffer(value=value)
                datatype = sniff.get_type()

                header = Header(csv_header, datatype)
                csv_header_info.append(header)

            return csv_header_info

    def get_header_names(self) -> [Header]:
        with open(self.file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            csv_headers = next(csv_reader)
            return csv_headers
