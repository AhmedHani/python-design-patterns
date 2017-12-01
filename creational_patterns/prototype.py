import copy as cp


class Sentence(object):

    def __init__(self, sentence, language):
        self.__sentence = sentence
        self.__language = language

    def get_sentence(self):
        return self.__sentence


class Prototype(object):

    @staticmethod
    def clone(object):
        return cp.deepcopy(object)

sentence = Sentence("Ahmed Hani", "English")
new_sentence = Prototype.clone(sentence)

print(sentence.get_sentence())
print(new_sentence.get_sentence())
