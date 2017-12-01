from source.calc import Math
import unittest


class TestSumMethod(unittest.TestCase):

    def test_basic(self):
        """
        Calcul the sum of a list of number
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

        expected = 6389
        result = Math.sum(data)

        self.assertEqual(result, expected)

    def test_one_value(self):
        """
        Calcul the sum of a list of number
        There is only ONE value
        """

        data = [
            186.0
        ]

        expected = 186
        result = Math.sum(data)

        self.assertEqual(result, expected)

    def test_no_value(self):
        """
        Calcul the sum of a list of number
        The list is empty
        """

        data = list()

        expected = 0
        result = Math.sum(data)

        self.assertEqual(result, expected)
