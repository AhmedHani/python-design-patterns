import random


class WordEmbedding(object):
    sentence = ""

    @classmethod
    def set_sentence(cls, sentence):
        cls.sentence = sentence

    @classmethod
    def factory(cls, type):
        if type == "Word2vec":
            return Word2Vec(cls.sentence)

        if type == "GloVe":
            return GloVe(cls.sentence)


class Word2Vec(WordEmbedding):

    def __init__(self, sentence):
        self.__sentence = sentence

    def vectorize(self):
        print("Word2vec")

    def get_sentence(self):
        return self.__sentence


class GloVe(WordEmbedding):

    def __init__(self, sentence):
        self.__sentence = sentence

    def vectorize(self):
        print("Glove")

    def get_sentence(self):
        return self.__sentence

WordEmbedding.sentence = "Ahmed Hani"
model = WordEmbedding.factory("GloVe")

model.vectorize()
print(type(model))