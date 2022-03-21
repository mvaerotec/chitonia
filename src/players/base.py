

class Base:

    def __init__(self):
        raise NotImplementedError("This class must not be initialized")

    def amar(self, other):
        if not isinstance(other, self.list_to_love):
            raise RuntimeError("Vete feo no che quien erech")
        else:
            other.recibir_amor(self)

    def say(self, words):
        print(f"{self.name} says: {words}")

    def recibir_amor(self, other):
        raise NotImplementedError("This method must be overwritten")
