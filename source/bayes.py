from parser import Parser
from calc import Math
import sys
import math


class Bayes:

    def __init__(self, horizontal_index):
        """
        Constructor
        :param horizontal_index: The index we want to learn about
        """

        self.horizontal_index = horizontal_index
        self.learned = list()

    def learn(self, data_path):
        """
        Learn from a file of data
        :param data_path: The path of the file of data
        :return:
        """
        # Split all data in each options of the columns we want
        parser = Parser(data_path)
        subgroups = parser.create_subgroup(self.horizontal_index)

        # Calcul variance and mean for each column of each subgroup
        variance = dict()
        mean = dict()
        for subgroup in subgroups:
            variance[subgroup] = dict()
            mean[subgroup] = dict()
            for name in parser.index:
                if name != self.horizontal_index:
                    values = parser.get_values(name, data=subgroups[subgroup])
                    variance[subgroup][name] = Math.variance(values)
                    mean[subgroup][name] = Math.mean(values)

        # Return a big array result with variance and mean of each subgroup
        result = list()

        line = list()
        line.append(self.horizontal_index)
        for name in parser.index:
            if name != self.horizontal_index:
                line.append('mean_' + name)
                line.append('variance_' + name)
        result.append(line)

        for subgroup in subgroups:
            line = list()

            line.append(subgroup)
            for name in parser.index:
                if name != self.horizontal_index:
                    line.append(mean[subgroup][name])
                    line.append(variance[subgroup][name])

            result.append(line)

        self.learned = result

    def classify(self, data):
        """
        Find the class of a new line
        :param data: The line we want to determine to classify
        :return: The class this algorithm determined
        """
        result = dict()

        for subgroup in self.learned[1:]:
            count = 0
            proba = None
            for column in data:
                mean = subgroup[count*2 + 1]
                variance = subgroup[count*2 + 2]
                if proba is not None:
                    proba *= Math.proba_column_given_class(
                        column,
                        variance,
                        mean
                    )
                else:
                    proba = Math.proba_column_given_class(
                        column,
                        variance,
                        mean
                    )

                count += 1

            result[subgroup[0]] = proba

        max_known = 0
        index = ""
        for elem in result:
            if result[elem] > max_known:
                max_known = result[elem]
                index = elem

        return index

    def _calcul_variance(parser):
        index = parser.index
        variance = dict()
        for name in index:
            if name != 'Sexe':
                variance[name] = Math.variance(parser.get_values(name))

        print(variance)
