import abc


class Word2vec(object):
    pass


class Builder(metaclass=abc.ABCMeta):

    def __init__(self):
        self.__word2vec = Word2vec()

    @abc.abstractmethod
    def build_sentence(self):
        pass

    @abc.abstractmethod
    def build_vocab(self):
        pass


class Word2vecBuilder(Builder):

    def __init__(self):
        super(Word2vecBuilder, self).__init__()

    def build_sentence(self):
        pass

    def build_vocab(self):
        pass


class Manager(object):

    def __init__(self, builder):
        self.__builder = builder

    def construct(self):
        self.__builder.build_sentence()
        self.__builder.build_vocab()


builder = Word2vecBuilder()
manager = Manager(builder)

manager.construct()

