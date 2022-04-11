from unittest import TestCase
from model import PatientData


class TestPatientData(TestCase):
    def setUp(self) -> None:
        self.under_test = PatientData()

    def test_model_get_gender_value(self):
        self.under_test.gender = 1
        self.assertEqual(self.under_test.getGenderValue(), "Male")
        self.under_test.gender = 0
        self.assertEqual(self.under_test.getGenderValue(), "Female")

    def test_model_get_cp_value(self):
        self.under_test.cp = 0
        self.assertEqual(self.under_test.getCpValue(), "Typical angina")
        self.under_test.cp = 1
        self.assertEqual(self.under_test.getCpValue(), "Atypical angina")
        self.under_test.cp = 2
        self.assertEqual(self.under_test.getCpValue(), "Non-anginal pain")
        self.under_test.cp = 3
        self.assertEqual(self.under_test.getCpValue(), "Asymptomatic")
        self.under_test.cp = 4
        self.assertEqual(self.under_test.getCpValue(), "Not recognized")

    def test_model_get_slope_value(self):
        self.under_test.slope = 1
        self.assertEqual(self.under_test.getSlopeValue(), "Upsloping")
        self.under_test.slope = 2
        self.assertEqual(self.under_test.getSlopeValue(), "Flat")

    def test_model_get_thal_value(self):
        self.under_test.thal = 1
        self.assertEqual(self.under_test.getThalValue(), "Normal")
        self.under_test.thal = 2
        self.assertEqual(self.under_test.getThalValue(), "Fixed defect")
        self.under_test.thal = 3
        self.assertEqual(self.under_test.getThalValue(), "Reversable defect")

    def test_model_get_exang_value(self):
        self.under_test.exang = 0
        self.assertEqual(self.under_test.getExangValue(), "No")
        self.under_test.exang = 1
        self.assertEqual(self.under_test.getExangValue(), "Yes")
