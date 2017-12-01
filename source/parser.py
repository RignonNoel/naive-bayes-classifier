import codecs


class Parser:

    def __init__(self, filename):
        self.filename = filename
        self.index = dict()

        self.data = self.import_list()

    def read_content(self):
        """
        Return the content of the datafile
        """

        file = codecs.open(self.filename, "r", "utf-8")
        content = file.readlines()
        file.close()

        return content

    def import_list(self):
        """
        Return a list of all number in the datafile
        """
        content = self.read_content()
        data = list()

        count = 0
        for line in content:
            if count > 0:
                # We populate the data array
                colonnes = line.split(";")
                content_line = list()

                for element in colonnes:
                    number = element.rstrip()
                    try:
                        number = float(number)
                    except ValueError:
                        pass
                    content_line.append(number)

                data.append(content_line)
            else:
                # We populate the index dictionary
                colonnes = line.split(";")
                index_number = 0
                for element in colonnes:
                    element = element.rstrip()
                    self.index[element] = index_number
                    index_number += 1
            count += 1
        return data

    def get_value(self, vertical_index, horizontal_index):
        """
        Return a value from the imported array
        :param vertical_index: Vertical index of the value
        :param horizontal_index: Horizontal index of the value
        :return: The value at this given position in the array
        """
        horizontal_index = self.find_index(horizontal_index)
        return self.data[vertical_index][horizontal_index]

    def get_values(self, horizontal_index, data=None):
        """
        Return all values of a given index
        :param horizontal_index: Horizontal index of the column
        :return: The list of values in this given column
        """
        # Check arguments
        horizontal_index = self.find_index(horizontal_index)

        if data is None:
            data = self.data

        # Init variables
        list_data = list()

        # Calculation
        for line in data:
            list_data.append(line[horizontal_index])

        return list_data

    def find_index(self, index):
        """
        Return an ID of index in function of the name of this one
        :param index: The name or the number of the index
        :return: The number of the index
        """
        if type(index) is int:
            # It's already an integer, so we return this integer
            return index
        else:
            # It's not an integer, so we try to find
            # the integer with the dictionary
            return self.index[index]

    def create_subgroup(self, horizontal_index):
        """
        Create each subgroup of a given column
        :param horizontal_index: The column we want to split in subgroup
        :return: A dictionnary with all subgroup splitted by value
        """
        horizontal_index = self.find_index(horizontal_index)

        subgroup = dict()

        for line in self.data:
            if not line[horizontal_index] in subgroup.keys():
                subgroup[line[horizontal_index]] = list()

            subgroup[line[horizontal_index]].append(line)

        return subgroup
