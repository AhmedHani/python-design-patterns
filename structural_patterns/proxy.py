from abc import ABCMeta, abstractmethod


class ISentence:
    __metaclass__ = ABCMeta

    def __init__(self, sentence):
        self.sentence = sentence

    @abstractmethod
    def get_grams(self, n):
        raise NotImplementedError("You must implement this function!")

    @abstractmethod
    def get_unique_words(self):
        raise NotImplementedError("You must implement this function!")


class ProcessingProxy(ISentence):

    def __init__(self, sentence):
        super().__init__(sentence)

    def get_grams(self, n):
        grams = []

        for i in range(0, len(self.sentence)):
            temp_grams = []

            if i + n > len(self.sentence):
                break

            for j in range(i, i + n):
                temp_grams.append(self.sentence[j])

            grams.append(temp_grams)

        return grams

    def get_unique_words(self):
        return list(set(self.sentence))


proxy = ProcessingProxy("My name is is Ahmed".split())
print(proxy.get_grams(2))
print(proxy.get_unique_words())





