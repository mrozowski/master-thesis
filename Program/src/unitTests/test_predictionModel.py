from unittest import TestCase
from config import message
from predictionModel import generateResult


class Test(TestCase):
    def test_generate_result_sick(self):
        under_test = generateResult(1, 0.9)
        self.assertEqual(under_test, message["SICK"])

    def test_generate_result_healthy(self):
        under_test = generateResult(0, 0.1)
        self.assertEqual(under_test, message["HEALTHY"])

    def test_generate_result_inconclusive(self):
        under_test = generateResult(1, 0.5)
        self.assertEqual(under_test, message["INCONCLUSIVE"])

