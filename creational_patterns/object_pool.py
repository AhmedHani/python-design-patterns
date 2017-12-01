

class Sentence(object):

    def __init__(self, sentence="Ahmed", language="Hani"):
        self.__sentence = sentence
        self.__language = language

    def get_sentence(self):
        return self.__sentence


class ObjectsManager(object):

    def __init__(self, size):
        self.__pool = [Sentence() for i in range(0, size)]

    def get(self):
        return self.__pool.pop()

    def put(self, sentence_object):
        self.__pool.append(sentence_object)

manager = ObjectsManager(5)

sentence = manager.get()
manager.put(sentence)