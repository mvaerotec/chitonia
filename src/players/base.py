

class Base:
    """
    Base class for the rest of the players, used as their parent class.
    Contains some methods that are common to all and also some methods that
    must be overriden in each subclass.
    """

    def __init__(self):
        raise NotImplementedError("This class must not be initialized")

    def love(self, other=None):
        """
        Main method for 'Love' action. It checks if `other` is within the
        player list of love and, if yes, it calls the `receive_love`
        method from the other player.
        """
        if isinstance(other, self.list_love):
            other.receive_love(self)
        elif isinstance(other, self.__class__):
            self.say("Como me amo yo a mí mismo????")
        else:
            self.no_love()

    def update(self, alr_trig):
        """
        Called at the end of each iteration, in order to update certain values

        These values depend on the player

        Returns whether a random action has been triggered or not, to prevent
        triggering more than one action each turn
        
        Receives as an argument whether an action has been already triggered
        """
        raise NotImplementedError("This method must be overriden")
        
    def say(self, words):
        """
        Prints a message in the output prepending the player's name, to 
        identify who says each message.
        """
        print(f"{self.name} says: {words}")

    def recibir_amor(self, other):
        """
        This method describes the action to perform in case the player is
        given love by `other`. Must be overriden in each of the players,
        as behaviour depends on each player
        """
        raise NotImplementedError("This method must be overriden")

    def action_possible(self):
        """
        Returns whether the player is available to perform and action or not.
        Must be overriden in each player.
        """
        raise NotImplementedError("This method must be overriden")
