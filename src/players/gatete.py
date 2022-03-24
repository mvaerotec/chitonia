
from .base import Base

from ..game_end_exception import GameEndException
from ..utils import *

import random

class Gatete(Base):
    """
    A gatete, pichu, averno, avernario milenario, forma, signiore, 
    paichupollo. In fact, anything but Zeus, that's for sure.

    He likes to play like an averno. He does not like love, and for sure he
    will point to the floor if loved. If you are lucky, he may be willing to
    amasar you, but I wouldn't hope for it (rare cases)
    """

    def __init__(self):
        self.name = "Gatete"
        
        self.maaaa()
        self.state = "averning"
        self.points = Points.INITIAL_VAL

        self.possible_states = [
            "averning",
            "fiesta",
            "rec_lov",
            "dormido",
            "hambriento",
            "muy_hambriento"
        ]

        self.list_love = ()

        self.available_actions = {
            "Jugar": self.play,
            "Amar": self.love,
            "Amasar": self.amasar
        }

        self.p_ni_caso = 0.3
        self.p_tranquilo = 0.2
        self.p_hambre = 0.2

    # Overriden methods
    def hello(self):
        """
        During hello (and in many other situations), he will say maaa
        """
        self.maaaa()
    
    def receive_love(self, other):
        """
        Gato does not like love, no matter who is the other. He is a gatete
        """
        self.maaaa()
        self.state = "rec_lov"
        self.point("suelo")
        other.points += Points.MED_INC
    
    def action_possible(self):
        """
        Gatete is an avernario milenario. There would be times when he is not
        in the mood, and he will run away. Gatete
        """
        if random.random() < self.p_ni_caso:
            self.maaaa()
            print("*Parece que a gato no le ha apetecido*")
            return False
        return True

    def update(self, alr_trig):
        """
        This method checks if he is hambriento, in which case he will let you
        know. Also, and randomly, gatete may start feeling hungry or stay
        quiet.

        Tip: if he is quiet, maybe he may be willing to amasar...
        """
        action_trig = False
        if self.state == "hambriento":
            self.maaaa()
            self.say("*Acabo de tirarte la mitad de cosas de la mesa, " +\
                "levantate yaaaaaa")
            self.state = "muy_hambriento"
        elif self.state == "muy_hambriento":
            self.maaaa()
            self.maaaa()
            self.say("*Me he puesto a comer triskis porque no me has dado de comer, "+\
                "sientete mal gentuzo")
            raise GameEndException("Te sientes mal porque gatete ha ido a comer sin ti, "+\
                "no le has hecho caso.")
        elif random.random() < self.p_hambre and not alr_trig:
            self.say("*Son las 7 de la mañana, hora de desayunar*")
            self.maaaa()
            self.state = "hambriento"
            action_trig = True

        if random.random() < self.p_tranquilo and self.state != "hambriento":
            self.state = "tranquilo"

        self.points -= Points.DECREASE

        return action_trig


    # Action methods
    def point(self, where):
        """
        If you give love to gatete, it is very likely that he points down
        """
        if self.state == "rec_lov" and where != "suelo": 
            raise RuntimeError("Gato antena directiva")
        return

    def maaaa(self):
        """
        It's a paichucat, and, obviously, says maaaa

        This is the most basic method from Gato. I think I've never used a
        function in a class more than this one.
        """
        self.say("MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

    def no_love(self):
        """
        Considering gato, it is highly probable that he does not want to give
        love. He is just going to say maaaa
        """
        self.maaaa()

    def play(self, item):
        """
        He is a gato, he wants fiesta.

        Changes his state to fiesta, and, depending on the item to play with
        performs an action.

        Available items are: raton, palo, tapon, chitamano

        If no item (or unknown) is given, gato acecha cual avernario milenario
        """
        self.state = "fiesta"
        if item == "raton":
            self.say("u u u u u u u u")
        elif item == "palo":
            self.say("*Ataca*")
        elif item == "tapon":
            self.say("*Lo ha colado debajo de la nevera*")
        elif item == "chitamano":
            self.say("*Muerde la mano incesantemente cual avernario milenario*")
        else:
            self.say("*Acecha*")

        self.points += Points.BIG_INC

    def amasar(self, other):
        if self.state == "tranquilo":
            self.say("PRRRRRRRRRRRRR")
            self.points += Points.BIG_INC
        else:
            self.maaaa()
            self.say("*Se ha ido corriendo, qué esperabas?*")
            self.points += Points.SMALL_INC
