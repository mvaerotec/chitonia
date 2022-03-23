import random

from .base import Base
from ..utils import *
from ..game_end_exception import GameEndException

class Pomtito(Base):
    def __init__(self):
        self.name = "Pomtito"

        # Importing inside init to avoid circular import
        from .gatete import Gatete
        from .chita import Chita
        from .chito import Chito
        from .mamichita import Mamichita
        self.list_love = (Chita, Chito, Gatete, Mamichita)

        self.state = "vaguete"
        self.available_states = ["felis", "vaguete", "broncas", "asesino"]

        self.p_paseo = 0.6
        self.p_pomtito_guau = 0.1

        self.available_actions = {
            "Amar": self.love,
            "Ladrar": self.guau,
            "Pasear": self.pasear
        }

    def guau(self):
        """
        He is a pomtito, he barks to the air
        """
        self.state = "broncas"
        self.say("GUAU GUAU GUAU GUAU GUAU GUAU!")
    

    def pasear(self):
        """
        Maybe he wants to, maybe not
        """
        if random.random() < self.p_paseo:
            self.state = "felis"
            self.say("*Saltitos y quiero paseo*")
            self.say("*He hecho pomkipis*")
        else:
            self.state = "vaguete"
            self.say("*Se ha metido debajo de la mesa*")

    # Overriden
    def update(self):
        """
        Method to run at the end of each loop iteration. In this case, the loop
        is the following:

        - If pomtito finds someone (randomly), he will be sent to 'broncas'
        state and needs to be calmed down
        - If pomtito is in broncas state, he will become even more angry and 
        needs to be calmed down. State is set to 'asesino'
        - If pomtito is in state asesino and not calmed down, he will kill 
        someone and game will end

        :return: None
        """

        if self.state == "asesino":
            self.say("*He matado a alguien sin querer, lo siento*")
            raise GameEndException("Pomtito ha matado a alguien")
        elif self.state == "broncas":
            self.guau()
            self.guau()
            self.say("*Pomtito está muy cabreado, deberías hacer algo...*")
            self.state = "asesino"
        elif random.random() < self.p_pomtito_guau:
            self.guau()
            self.say("*He oído algo y le he tenido que echar la pomkibronca*")
            self.state = "broncas"
        return
        
    def receive_love(self, other):
        if isinstance(other, self.list_love):
            self.state = "felich"
            self.say("*Pomtito felis, le gusta el amor*")
        else:
            self.guau()

    def action_possible(self):
        """
        Determines if the action can be done or not
        """
        return True

    def hello(self):
        """
        Pontito es felis cachi chiempre
        """
        if self.state == "broncas" or self.state == "asesino":
            self.guau()
        else:
            self.say("*Pomtito felis*")