import copy as cp


class Sentence(object):

    def __init__(self, sentence):
        self.__sentence = sentence
        self.__momento = {1: cp.deepcopy(self)}

    def to_lower(self):
        self.__sentence = self.__sentence.lower()

        self.__add_momento()

    def to_upper(self):
        self.__sentence = self.__sentence.upper()

        self.__add_momento()

    def get_moments(self):
        return self.__momento

    def get_moment(self, state):
        return self.__momento[state]

    def get_sentence(self):
        return self.__sentence

    def __add_momento(self):
        self.__momento[len(self.__momento) + 1] = cp.deepcopy(self)


sentence = Sentence("Ahmed Hani")
print(sentence.get_moments()[1].get_sentence())
sentence.to_upper()
print(sentence.get_moments()[2].get_sentence())
sentence = sentence.get_moment(1)
print(sentence.get_sentence())






