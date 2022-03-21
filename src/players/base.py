

class Base:

    def __init__(self):
        raise NotImplementedError("This class must not be initialized")

    def amar(self, other):
        if not isinstance(other, self.list_to_love):
            self.no_love()
        else:
            other.recibir_amor(self)

    def update(self):
        raise NotImplementedError("This method must be overwritten")
        
    def say(self, words):
        print(f"{self.name} says: {words}")

    def recibir_amor(self, other):
        raise NotImplementedError("This method must be overwritten")

    def action_possible(self):
        """
        Determines if the action can be done or not
        """
        raise NotImplementedError("This method must be overwritten")
