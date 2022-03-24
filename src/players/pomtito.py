import random

from .base import Base
from ..utils import *
from ..game_end_exception import GameEndException

class Pomtito(Base):
    """
    He is a pomtito, paionch, beauty, triple/cuadruple/quintuple plaionch,
    bellezo, pomtibebe, etc.

    He is amoroso with the people he knows, but he wants to kill some people
    (basically anyone that is able to breathe). Be careful if he starts to
    bark as, even if he does not look like it, he is a dangerous creature
    """
    def __init__(self):
        self.name = "Pomtito"

        # Importing inside init to avoid circular import
        from .gatete import Gatete
        from .chita import Chita
        from .chito import Chito
        from .mamichita import Mamichita
        self.list_love = (Chita, Chito, Gatete, Mamichita)

        self.state = "felis"
        self.available_states = ["felis", "vaguete", "broncas", "asesino"]
        self.points = Points.INITIAL_VAL

        self.action_guau = False

        self.p_paseo = 0.6
        self.p_pomtito_guau = 0.1
        self.p_inaction = 0.3

        self.available_actions = {
            "Amar": self.love,
            "Ladrar": self.guau,
            "Pasear": self.pasear
        }

    def guau(self):
        """
        He is a pomtito, he barks to the air

        State is set to `broncas`, so be careful and do something or he may
        get dangerous...
        """
        self.state = "broncas"
        self.action_guau = True
        self.say("GUAU GUAU GUAU GUAU GUAU GUAU!")
    

    def pasear(self):
        """
        Maybe he wants to, maybe not. Pure luck
        """
        if random.random() < self.p_paseo:
            self.state = "felis"
            self.say("*Saltitos y quiero paseo*")
            self.say("*He hecho pomkipis*")
            self.points += Points.BIG_INC
        else:
            self.state = "vaguete"
            self.say("*Se ha metido debajo de la mesa*")
            self.points += Points.MED_INC

    # Overriden
    def update(self, alr_trig):
        """
        Method to run at the end of each loop iteration. In this case, the loop
        is the following:

        - If pomtito finds someone (randomly), he will be sent to 'broncas'
          state and needs to be calmed down
        - If pomtito is in broncas state, he will become even more angry and 
          needs to be calmed down. State is set to 'asesino'
        - If pomtito is in state asesino and not calmed down, he will kill 
          someone and game will end
        """

        action_trig = False
        if self.state == "asesino":
            self.say("*He matado a alguien sin querer, lo siento*")
            raise GameEndException("Pomtito ha matado a alguien")
        elif self.state == "broncas" and not self.action_guau:
            self.guau()
            self.guau()
            self.say("*Pomtito está muy cabreado, deberías hacer algo...*")
            self.state = "asesino"
        elif random.random() < self.p_pomtito_guau and not alr_trig:
            self.guau()
            self.say("*He oído algo y le he tenido que echar la pomkibronca*")
            self.state = "broncas"
            action_trig = True
        self.action_guau = False

        self.points -= Points.DECREASE

        return action_trig
        
    def receive_love(self, other):
        """
        A pomtito is a cocha mimochi, and likes to receive love. But don't
        try if you don't know him, you can end up really bad...
        """
        if isinstance(other, self.list_love):
            self.state = "felich"
            self.say("*Pomtito felis, le gusta el amor*")
            self.points += Points.BIG_INC
            other.points += Points.SMALL_INC
        else:
            self.say("*Me lo acabo de cargar*")
            self.guau()

    def action_possible(self):
        """
        Determines if the action can be done or not
        """
        if self.state == "vaguete" and random.random() < self.p_inaction:
            self.say("*Pomtito está vaguete, va a cher que añoma*")
            return False
        return True

    def hello(self):
        """
        Pontito es felis cachi chiempre
        """
        if self.state == "broncas":
            self.guau()
        elif self.state == "asesino":
            self.say("ME LO CARGO, ME LO CARGO")
        else:
            self.say("*Pomtito felis*")
            self.points += Points.SMALL_INC
    
    def no_love(self):
        self.guau()