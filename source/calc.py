import math


class Math:

    def __init__(self):
        pass

    @staticmethod
    def sum(list_data):
        """
        Return the sum of the list
        """

        total = 0
        for number in list_data:
            total += number

        return total

    @staticmethod
    def mean(list_data):
        """
        Return the mean of the list
        """

        total = Math.sum(list_data)
        mean = total / float(len(list_data))

        return mean

    @staticmethod
    def variance(list_data):
        """
        Return the variance of the list
        """

        mean = Math.mean(list_data)
        sum_distance = 0

        for number in list_data:
            distance = (number - mean) * (number - mean)
            sum_distance += distance

        variance = (1 / float((len(list_data) - 1))) * sum_distance

        return variance

    @staticmethod
    def proba_column_given_class(value, variance, mean):
        first_argument = 1 / float((math.sqrt(2 * math.pi * variance)))

        nominator = -((value - mean) * (value - mean))
        denominator = 2 * variance
        second_argument = math.exp(nominator / float(denominator))

        probability = first_argument * second_argument
        return probability
