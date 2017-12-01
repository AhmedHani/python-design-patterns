

class LogisticRegression(object):

    def __init__(self, learning_rate=0.1):
        self.__learning_rate = learning_rate

    def fit(self, x_train, y_train):
        pass

    def predict(self, x_test):
        pass


class SupportVectorMachine(object):

    def __init__(self, kernel_name='gaussian'):
        self.__kernel_name = kernel_name

    def fit(self, x_train, y_train):
        pass

    def predict(self, x_test):
        pass


class BinaryClassifier(object):

    def __init__(self):
        self.__logistic_regression = LogisticRegression()
        self.__support_vector_machine = SupportVectorMachine()

    def train(self, x_train, y_train):
        self.__logistic_regression.fit(x_train, y_train)
        self.__support_vector_machine.fit(x_train, y_train)

    def test(self, x_test):
        self.__logistic_regression.predict(x_test)
        self.__support_vector_machine.predict(x_test)

binary_classifier = BinaryClassifier()
