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
        self.prev_state = "chiteante"
        self.points = Points.INITIAL_VAL

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
            "Amar": self.love,
            "Alimentar": self.alimentar
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

        He becomes happy. Does not remove `liada` state

        """
        from .gatete import Gatete
        from .chita import Chita
        from .mamichita import Mamichita
        from .pomtito import Pomtito
        if isinstance(other, Chita):
            self.say("PRRRRRRRR MIMICH QUE FELIS")
            self.points += Points.BIG_INC
            other.points += Points.MED_INC
        elif isinstance(other, Gatete):
            self.say("GATETE DAME AMOR TU")
            other.maaaa()
            self.points += Points.BIG_INC
            other.points += Points.SMALL_INC
        elif isinstance(other, Pomtito):
            self.say("AÑAÑA")
            self.points += Points.BIG_INC
            other.points += Points.MED_INC
        elif isinstance(other, Mamichita):
            self.say("Que monaaa")
            self.points += Points.MED_INC
            other.points += Points.SMALL_INC
        else:
            self.say("No che quien erech feo ma")

        if self.state != "liada" or self.prev_state != "liada":
            self.state = "felis"
            self.prev_state = "felis"

    def action_possible(self):
        """
        Chito does not have siesta time or anything that can make him
        inactive
        """
        return True

    def update(self, alr_trig):
        if self.state == "trichte":
            self.say("PRRRRRRRRRR")
            if self.prev_state == "mimochi":
                msg = "Chito echta trichte y no ha rechibido mimich"
            elif self.prev_state == "liada":
                msg = "Chito echta trichte y no le has ayudado ma"
            raise GameEndException(msg)
        elif self.state == "mimochi":
            self.say("POR QUE NO TENGO MIMICH")
            self.state = "trichte"
            self.prev_state = "mimochi"
        elif self.state == "liada":
            self.say("CHITAAAAAAAAAA AYUDAAAAAAAAAAAAA")
            self.state = "trichte"
            self.prev_state = "liada"

        action_trig = False
        if random.random() < self.p_mimich and self.state != "trichte" and not alr_trig:
            self.say("QUERO MIMICH")
            self.state = "mimochi"
            action_trig = True
        elif random.random() < self.p_mimich and self.state != "trichte" and not alr_trig:
            self.say("Chita la he liaaaaadooooooooooooooooo")
            self.state = "liada"
            action_trig = True

        self.points -= Points.DECREASE

        return action_trig

    def no_love(self):
        """
        Method to be called if you try to make chito love someone he does not
        know. In this case, he will refuse
        """
        self.say("Vete feo no che quien erech")

    def alimentar(self, other):
        """
        We need to keep other players in game feeded. The behavior of the
        other depends on who it is. This method can be used to prevent
        losing due to gatete's hunger
        """
        from .gatete import Gatete
        from .pomtito import Pomtito
        from .chita import Chita

        if isinstance(other, Gatete):
            other.state = "averning"
            self.say("QUIERE COMER MI CHICO PEQUEÑOOOO")
            other.say("*Comiendo triskitos*")
            other.maaaa()
            other.points += Points.BIG_INC
        elif isinstance(other, Pomtito):
            self.say("Toma pomkisiva, un chuletón")
            other.say("*Lo huele*")
            other.say("Que te lo comas tuuuuuuu")
            other.points += Points.MED_INC
        elif isinstance(other, Chita):
            if not other.siesta:
                other.say("Cocholate")
                other.points += Points.BIG_INC
                self.points += Points.MED_INC
            else:
                other.say("Dejame que estoy en la chiesta ma")
                other.points -= 1
