
from base import Base

class Mamichita(Base):

    def __init__(self):
        self.name = "Mamichita"
        

    def called_urraca(self):
        if not self.siesta:
            self.say("QUE QUIEEEEEEEEEEERES")