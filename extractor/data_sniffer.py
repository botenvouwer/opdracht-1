from dateutil import parser


class DataSniffer:

    def __init__(self, value):
        self.value = value

    def get_type(self):  # TODO : wanneer er meerdere datatypen in 1 kolom staan gaat het mis

        if self.is_integer():
            return "INTEGER"
        elif self.is_float():
            return "FLOAT"
        # elif self.is_datetime():
        #     return "DATETIME"
        #     pass
        else:
            return "TEXT"

    def is_integer(self):
        if self.value == '':
            return False
        else:
            try:
                int(self.value)
                return True
            except ValueError:
                return False

    def is_float(self):
        if self.value == '':
            return False
        else:
            try:
                float(self.value)
                return True
            except ValueError:
                return False

    def is_datetime(self):
        if self.value == '':
            return False
        else:
            try:
                parser.parse(self.value)
                return True
            except ValueError:
                return False

# Aangepaste is_datetime method die, wanneer deze een datatype datum herkend deze meteen herschrijft in het format
# wat Postgres prettig vindt.

# def is_datetime(self):
#     if self.value == '':
#         return False, None
#     else:
#         try:
#             parsed_date = parser.parse(self.value)
#             formatted_date = parsed_date.strftime('%Y-%m-%d')
#             return True, formatted_date
#         except ValueError:
#             return False, None
