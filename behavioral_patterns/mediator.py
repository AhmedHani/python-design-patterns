

class MachineLearning(object):

    def __init__(self, mediator):
        self.__mediator = mediator

    def get_mediator(self):
        return self.__mediator


class NaturalLanguageProcessing(object):
    def __init__(self, mediator):
        self.__mediator = mediator

    def get_mediator(self):
        return self.__mediator


class DataScience(object):

    def __init__(self):
        self.__ml = MachineLearning(self)
        self.__nlp = NaturalLanguageProcessing(self)

    def get_fields(self):
        return self.__ml, self.__nlp


data_science = DataScience()
print(type(data_science.get_fields()[0]).__name__,
      type(data_science.get_fields()[1]).__name__)
