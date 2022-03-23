from datetime import time

from .base import Base
from ..utils import is_time_between

class Mamichita(Base):

    def __init__(self):
        self.name = "Mamichita"

        self.state = "Mamichita"

        self.siesta_start = time(17,30)
        self.siesta_end = time(18,30)
        self.cayo_start = time(10,30)
        self.cayo_end = time(11,59)

        self.siesta = is_time_between(self.siesta_start, self.siesta_end)
        self.cayo = is_time_between(self.cayo_start, self.cayo_end)

        # Importing inside init to avoid circular import
        from .gatete import Gatete
        #from .pomtito import Pomtito
        #from .chito import Chito
        from .chita import Chita
        self.list_love = (Chita, Gatete)
        
        self.available_actions = {
            "Amar": self.love
        }

    # Overriden methods
    def action_possible(self):
        if self.siesta:
            self.say("Siesta time")
        elif self.cayo:
            self.say("No puede actuar, está hablando con Cayo")
        
        return not (self.siesta or self.cayo)

    def update(self):

        self.siesta = is_time_between(self.siesta_start, self.siesta_end)
        self.cayo = is_time_between(self.cayo_start, self.cayo_end)

    def hello(self):
        self.say("Holi")

    def no_love(self):
        self.say("No, no te toca")

    def called_urraca(self):
        """
        Chita likes to call like an urraca. Mamichita has to answer
        """
        if not self.siesta:
            if self.cayo:
                self.say("Que estoy hablandoooooo")
            else:
                self.say("QUE QUIEEEEEEEEEEERES")
        