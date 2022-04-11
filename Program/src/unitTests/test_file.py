from unittest import TestCase
from model import PatientData
from file import parseData, IncorrectFileFormatError


class Test(TestCase):
    def test_parse_csv(self):
        under_test = parseData(content=_csv_data())
        expected = _expected_result()
        self.assertEqual(under_test.name, expected.name)
        self.assertEqual(under_test.exang, expected.exang)
        self.assertEqual(under_test.gender, expected.gender)
        self.assertEqual(under_test.oldpeak, expected.oldpeak)

    def test_parse_csv_rise_exception_when_values_are_missing(self):
        missing_data = [["name", "age", "sex", "cp"], ["some name", "45", "0", "1"]]
        self.assertRaises(IncorrectFileFormatError, parseData, missing_data)

    def test_parse_csv_rise_exception_when_values_are_invalid(self):
        invalid_data = _csv_invalid_data()
        self.assertRaises(IncorrectFileFormatError, parseData, invalid_data)


def _expected_result():
    expected = PatientData()
    expected.name = "Marek Marecki"
    expected.age = 63
    expected.gender = 1
    expected.cp = 3
    expected.trestbps = 145
    expected.chol = 233
    expected.fbs = 1
    expected.restecg = 0
    expected.thalach = 150
    expected.exang = 0
    expected.oldpeak = 2.3
    expected.slope = 0
    expected.ca = 0
    expected.thal = 1
    return expected


def _csv_data():
    values = ["Marek Marecki", "63", "1", "3", "145", "233", "1", "0", "150", "0", "2.3", "0", "0", "1"]
    csv = [names, values]
    return csv


def _csv_invalid_data():
    values = ["Marek Marecki", "63", "1", "3", "145", "233", "1", "0", "150", "zero", "2.3", "0", "0", "1"]
    csv = [names, values]
    return csv


names = ["name", "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]