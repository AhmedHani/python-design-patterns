import abc


class WordEmbedding(metaclass=abc.ABCMeta):

    def __init__(self, sentence):
        self._sentence = sentence

    @abc.abstractmethod
    def vectorize(self):
        pass


class Word2vec(WordEmbedding):

    def __init__(self, sentence):
        super(Word2vec, self).__init__(sentence)

    def vectorize(self):
        pass


class Glove(WordEmbedding):
    def __init__(self, sentence):
        super(Glove, self).__init__(sentence)

    def vectorize(self):
        pass


class Model(object):

    def __init__(self, embedding_model):
        self.__embedding_model = embedding_model

    def run_model(self):
        self.__embedding_model.vectorize()

model = Model(Word2vec("Ahmed Hani"))
