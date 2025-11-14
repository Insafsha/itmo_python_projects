import xml.dom.minidom as minidom


def parse_currency(path):
    xml_data = open(path, encoding='windows-1251').read()
    dom = minidom.parseString(xml_data)
    dom.normalize()

    char_codes = []
    values = []

    for valute in dom.getElementsByTagName("Valute"):
        char = valute.getElementsByTagName("CharCode")[0].firstChild.data
        value = valute.getElementsByTagName("Value")[0].firstChild.data
        value = float(value.replace(',', '.'))

        char_codes.append(char)
        values.append(value)

    return char_codes, values
