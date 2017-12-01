from bayes import Bayes

# First you need to create an instance of this
# algorithm and defined what field/column
# you want to classify
instance = Bayes("Sex")

# Secondly, you will need to learn about a set
# of data to train the algorithm
instance.learn("static/data_test.csv")

# Finally you can use your trained instance to
# classify a set of data (In this example we
# will find the most probable sex)
print(instance.classify([6, 130, 8]))
