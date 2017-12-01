from source.calc import Math
import unittest


class TestVarianceMethod(unittest.TestCase):

    def test_basic(self):
        """
        Calcul the variance of a list of number
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

        expected = 391417.8777777777
        result = Math.variance(data)

        self.assertEqual(result, expected)

    def test_one_value(self):
        """
        Calcul the variance of a list of number
        The list have only ONE number
        """

        data = [
            186.0
        ]

        expected = "ZeroDivisionError"

        try:
            result = Math.variance(data)
        except ZeroDivisionError:
            result = "ZeroDivisionError"

        self.assertEqual(result, expected)

    def test_two_value(self):
        """
        Calcul the variance of a list of number
        The list have only TWO number
        """

        data = [
            186.0,
            192.3
        ]

        expected = 19.84500000000007
        result = Math.variance(data)

        self.assertEqual(result, expected)
