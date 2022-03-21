import numpy as np
from datetime import time

from base import Base
from gatete import Gatete
from chito import Chito
from pomtito import Pomtito
from mamichita import Mamichita
from .utils import *

class Chito(Base):
    """
    Class to represent a chitonchito que diche maaaa y quere mucho a chitonita
    """

    def __init__(self):
        self.name = "Chito"

        self.state = "chiteante"

        self.possible_states = ["chiteante", "felis", ]

        self.estado_civil = "chiteado"

        self.list_to_love = (Chito, Gatete, Pomtito, Mamichita)

        self.available_actions = {
            "Amar": self.amar,
            ""
        }

    def hello(self):
        self.holi()
    
    def holi(self):
        self.say("Holiiiii")

    # Reception methods
    def recibir_amor(self, other):
        if isinstance(other, self.list_to_love):
            self.say("AÑAÑA")
        if isinstance(other, Chita):
            self.say("PRRRRRRRR MIMICH QUE FELIS")
            self.state = "felis"

    def action_possible(self):
        return True

    def update(self):
        return