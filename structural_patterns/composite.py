from abc import ABCMeta, abstractmethod


class LearningAlgorithm:
    __metaclass__ = ABCMeta

    @abstractmethod
    def fit(self, x_train, y_train):
        raise NotImplementedError("You must implement this function!")

    def predict(self, x_test):
        raise NotImplementedError("You must implement this function!")


class LogisticRegression(LearningAlgorithm):

    def __init__(self, learning_rate):
        self.__learning_rate = learning_rate

    def fit(self, x_train, y_train):
        pass

    def predict(self, x_test):
        pass


class NeuralNetwork(LearningAlgorithm):

    def __init__(self, learning_rate):
        self.__learning_rate = learning_rate

    def fit(self, x_train, y_train):
        pass

    def predict(self, x_test):
        pass


class MachineLearningPackage:

    def __init__(self):
        self.__algorithms = []

    def add_algorithm(self, algorithm):
        self.__algorithms.append(algorithm)

    def print_algorithm(self):
        for algorithm in self.__algorithms:
            print(type(algorithm).__name__)

machine_learning = MachineLearningPackage()
machine_learning.add_algorithm(LogisticRegression(0.1))
machine_learning.add_algorithm(NeuralNetwork(0.1))

machine_learning.print_algorithm()
