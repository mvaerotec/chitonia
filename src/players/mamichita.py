
from base import Base

class Mamichita(Base):

    def __init__(self):
        self.name = "Mamichita"

        self.siesta = False
        

    def called_urraca(self):
    """
    Chita likes to call like an urraca. Mamichita has to answer
    """
        if not self.siesta:
            self.say("QUE QUIEEEEEEEEEEERES")