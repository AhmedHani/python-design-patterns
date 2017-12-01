import abc


class WordEmbedding(metaclass=abc.ABCMeta):

    def run(self, sentence):
        self.add_sentence(sentence)
        self.build_vocabulary()
        self.vectorize()

    @abc.abstractmethod
    def add_sentence(self, sentence):
        pass

    @abc.abstractmethod
    def build_vocabulary(self):
        pass

    @abc.abstractmethod
    def vectorize(self):
        pass


class Word2vec(WordEmbedding):

    def add_sentence(self, sentence):
        pass

    def build_vocabulary(self):
        pass

    def vectorize(self):
        pass


model = Word2vec()
model.run("Ahmed Hani")



