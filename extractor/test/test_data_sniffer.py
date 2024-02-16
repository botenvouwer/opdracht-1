from extractor.data_sniffer import DataSniffer


def test_data_sniffer_int():
    sniffer = DataSniffer('232')
    get_type = sniffer.get_type()

    assert get_type == 'INTEGER'


def test_data_sniffer_str():
    sniffer = DataSniffer('gfsfgsdhf')
    get_type = sniffer.get_type()

    assert get_type == 'TEXT'


def test_data_sniffer_not_text_with_int():
    sniffer = DataSniffer('662L')
    get_type = sniffer.get_type()

    assert get_type == 'TEXT'

def test_data_sniffer_datetime():
    sniffer = DataSniffer('04-12-1978')
    get_type = sniffer.get_type()

    assert get_type == 'DATETIME'

def test_data_sniffer_empty():
    sniffer = DataSniffer('')
    get_type = sniffer.get_type()

    assert get_type == 'TEXT'

def test_data_sniffer_datetime_2():
    sniffer = DataSniffer('1978-12-04')
    get_type = sniffer.get_type()

    assert get_type == 'DATETIME'

def test_data_sniffer_datetime_3():
    sniffer = DataSniffer('04/12/1978')
    get_type = sniffer.get_type()

    assert get_type == 'DATETIME'

def test_data_sniffer_float():
    sniffer = DataSniffer('65.7')
    get_type = sniffer.get_type()

    assert get_type == 'FLOAT'

def test_data_sniffer_gekke_tekens():
    sniffer = DataSniffer('Læàl')
    get_type = sniffer.get_type()

    assert get_type == 'TEXT'

def test_data_sniffer_float_2():
    sniffer = DataSniffer('65,7')
    get_type = sniffer.get_type()

    assert get_type == 'TEXT'