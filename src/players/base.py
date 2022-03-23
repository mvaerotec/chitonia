

class Base:

    def __init__(self):
        raise NotImplementedError("This class must not be initialized")

    def love(self, other):
        if isinstance(other, self.list_love):
            other.receive_love(self)
        elif isinstance(other, self.__class__):
            self.say("Como me amo yo a mí mismo????")
        else:
            self.no_love()

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
