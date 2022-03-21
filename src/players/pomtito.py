from base import Base
from gatete import Gatete
from chita import Chita
from chito import Chito
from mamichita import Mamichita
from .utils import *

class Pomtito(Base):
    def __init__(self):
        self.name = "Pomtito"

        self.list_love = [Chita, Chito, Gatete, Mamichita]

        self.state = "vaguete"
        self.available_states = ["felis", "vaguete", "broncas"]

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
        if random.rand() < self.p_paseo:
            self.state = "felis"
            self.say("*Saltitos y quiero paseo*")
            self.say("*He hecho pomkipis*")
        else:
            self.state = "vaguete"
            self.say("*Se ha metido debajo de la mesa*")

    # Overriden
    def update(self):
        if random.rand() < self.p_pomtito_guau:
            self.guau()
            self.say("*He oído algo y le he tenido que echar la pomkibronca*")
        return
        
    def recibir_amor(self, other):
        if isinstance(other, self.list_love):
            self.state = "felich"
        else:
            self.guau()

    def action_possible(self):
        """
        Determines if the action can be done or not
        """
        return True