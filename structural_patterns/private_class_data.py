

class SentenceData(object):
    def __init__(self, sentence, language):
        self.__sentence = sentence
        self.__language = language

    def get_sentence(self):
        return self.__sentence

    def get_language(self):
        return self.__language


class Sentence(object):
    def __init__(self, sentence, language):
        self.__sentence_data = SentenceData(sentence, language)

    def to_lower(self):
        return self.__sentence_data.get_sentence().lower()

    def to_upper(self):
        return self.__sentence_data.get_sentence().upper()

    def translate(self):
        pass

sentence = Sentence("Ahmed Hani", "English")
print(sentence.to_lower())
print(sentence.to_upper())

