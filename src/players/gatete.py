
from base import Base


class Gatete(Base):

    def __init__(self):
        self.maaaa()
        self.state = "averning"

    # Action methods
    def point(self, where):
        if self.state == "rec_lov" and where != "suelo": 
            raise RuntimeError("Gatoantenadirectiva")
        return

    def maaaa(self):
        self.say("MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

    # Reception methods
    def recibir_amor(self, other, quantity):
        self.maaaa()
        self.state = "rec_lov"
        self.point("suelo")

