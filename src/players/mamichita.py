from datetime import time

from .base import Base
from ..utils import *

class Mamichita(Base):
    """
    She is the mami of Chita. She loves Chita a lot and takes care of her and
    of chito when they need anything. She is also Gatete's novia, and both
    like to spend time together, overall during siesta
    """
    def __init__(self):
        self.name = "Mamichita"

        self.state = "Mamichita"
        self.points = Points.INITIAL_VAL

        self.siesta_start = time(17,30)
        self.siesta_end = time(18,30)
        self.cayo_start = time(10,30)
        self.cayo_end = time(11,59)

        self.siesta = is_time_between(self.siesta_start, self.siesta_end)
        self.cayo = is_time_between(self.cayo_start, self.cayo_end)

        # Importing inside init to avoid circular import
        from .gatete import Gatete
        from .pomtito import Pomtito
        from .chito import Chito
        from .chita import Chita
        self.list_love = (Chita, Gatete, Chito, Pomtito)
        
        self.available_actions = {
            "Amar": self.love
        }

    # Overriden methods
    def action_possible(self):
        """
        Unavailable during siesta (Chita inherited it from someone) and during
        the night, when she receives a phone call and you can say goodbye
        """
        if self.siesta:
            self.say("Siesta time")
        elif self.cayo:
            self.say("No puede actuar, está hablando con Cayo")
        
        return not (self.siesta or self.cayo)

    def update(self, alr_trig):
        """
        Updates the time of her siesta and of her phone conversations, for
        availability
        """
        self.siesta = is_time_between(self.siesta_start, self.siesta_end)
        self.cayo = is_time_between(self.cayo_start, self.cayo_end)
        
        if self.action_possible():
            self.points -= Points.DECREASE

        return False

    def hello(self):
        self.say("Holi")

    def no_love(self):
        self.say("No, no te toca")

    def called_urraca(self):
        """
        Chita likes to call like an urraca. Mamichita has to answer

        Don't expect an answer during siesta, and during phone conversations
        the answer may difer
        """
        if not self.siesta:
            if self.cayo:
                self.say("Que estoy hablandoooooo")
            else:
                self.say("QUE QUIEEEEEEEEEEERES")
                self.points += Points.MED_INC
    
    def receive_love(self, other):
        from .chita import Chita
        from .chito import Chito
        from .gatete import Gatete
        if isinstance(other, Chita):
            self.say("Pero merisinaaa")
            self.points += Points.BIG_INC
            other.points += Points.MED_INC
        elif isinstance(other, Gatete):
            self.say("Pero gato")
            self.points += Points.MED_INC
            other.points += Points.SMALL_INC
        elif isinstance(other, Chito):
            self.say("Hola! Que tal?")
            self.points += Points.SMALL_INC
            other.points += Points.SMALL_INC
        