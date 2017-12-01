from source.calc import Math
import unittest


class TestMeanMethod(unittest.TestCase):

    def test_basic(self):
        """
        Calcul the mean of a list of number
        """

        data = [
            186.0,
            699,
            132,
            272,
            291,
            331,
            199,
            1890,
            788,
            1601
        ]

        expected = 638.9
        result = Math.mean(data)

        self.assertEqual(result, expected)

    def test_one_value(self):
        """
        Calcul the mean of a list of number
        The list have only ONE number
        """

        data = [
            186.0
        ]

        expected = 186.0
        result = Math.mean(data)

        self.assertEqual(result, expected)

    def test_no_value(self):
        """
        Calcul the mean of a list of number
        The list is empty
        """

        data = list()

        expected = "ZeroDivisionError"

        try:
            result = Math.mean(data)
        except ZeroDivisionError:
            result = "ZeroDivisionError"

        self.assertEqual(result, expected)
