

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class LoadText(metaclass=Singleton):

    def __init__(self, file_path):
        self.__file_path = file_path

    def load_text(self):
        self.__sentence = "Permenant Text"

    def get_sentence(self):
        return self.__sentence

a = LoadText("path")
a.load_text()
print(a.get_sentence())

b = LoadText("path")
print(b.get_sentence())