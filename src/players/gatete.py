
from .base import Base

import random

class Gatete(Base):

    def __init__(self):
        self.name = "Gatete"
        
        self.maaaa()
        self.state = "averning"

        self.possible_states = ["averning", "fiesta", "rec_lov"]

        self.list_love = ()

        self.available_actions = {
            "Jugar": self.play,
            "Amar": self.love,
        }

        self.p_ni_caso = 0.3

    # Overriden methods
    def hello(self):
        self.maaaa()
    
    def receive_love(self, other):
        """
        Gato does not like love, no matter who is the other. He is a gatete
        """
        self.maaaa()
        self.state = "rec_lov"
        self.point("suelo")
    
    def action_possible(self):
        if random.random() < self.p_ni_caso:
            self.maaaa()
            print("*Parece que a gato no le ha apetecido*")
            return False
        return True

    def update(self):
        return

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
        This is the most basic method from Gato. I think I've never used a
        function in a class more than this.

        It's a paichucat, and, obviously, says maaaa
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
    

