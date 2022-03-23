import numpy as np
import random

from .base import Base
from ..utils import *
from ..game_end_exception import GameEndException


class Chito(Base):
    """
    Class to represent a chitonchito that says maaaa and loves chitonita a lot
    """

    def __init__(self):
        self.name = "Chito"

        self.state = "chiteante"

        self.possible_states = ["chiteante", "felis", "mimochi", "trichte"]

        self.estado_civil = "chiteado"
        self.p_mimich = 0.2
        self.p_liada = 0.2

        # Importing inside init to avoid circular import
        from .gatete import Gatete
        from .chita import Chita
        from .pomtito import Pomtito
        from .mamichita import Mamichita
        self.list_love = (Chita, Gatete, Pomtito, Mamichita)

        self.available_actions = {
            "Amar": self.love
        }

    def hello(self):
        """
        Welcome method for chito. He says holi if he is happy, he cries if sad
        """
        if self.state == "trichte":
            self.say("PRRRRRRRRRR")
            self.say("*Chito echta trichte*")
        else:
            self.say("Holiiiii")
    
    # Reception methods
    def receive_love(self, other):
        """
        He is a cocha mimocha. He likes to receive love

        If chita loves him, he becomes happy
        If gato or pom love him, he is not sad anymore
        """
        from .gatete import Gatete
        from .chita import Chita
        from .pomtito import Pomtito
        if isinstance(other, Chita):
            self.say("PRRRRRRRR MIMICH QUE FELIS")
            self.state = "felis"
        elif isinstance(other, Gatete):
            self.say("GATETE DAME AMOR TU")
            other.maaaa()
            self.state = "chiteante"
        elif isinstance(other, Pomtito):
            self.say("AÑAÑA")
            self.state = "chiteante"
        else:
            self.say("AÑAÑA")

    def action_possible(self):
        return True

    def update(self):
        if self.state == "trichte":
            self.say("PRRRRRRRRRR")
            raise GameEndException("Chito echta trichte y no ha rechibido mimich")
        elif self.state == "mimochi":
            self.say("POR QUE NO TENGO MIMICH")
            self.state = "trichte"
        elif self.state == "liada":
            self.say("CHITAAAAAAAAAA AYUDAAAAAAAAAAAAA")
            self.state = "trichte"

        if random.random() < self.p_mimich and self.state != "liada":
            self.say("QUERO MIMICH")
            self.state = "mimochi"
        elif random.random() < self.p_mimich and self.state != "mimochi":
            self.say("Chita la he liaaaaadooooooooooooooooo")
            self.state = "liada"
        return