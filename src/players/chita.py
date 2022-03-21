import numpy as np

from base import Base
from gatete import Gatete
from chito import Chito
from pomtito import Pomtito
from mamichita import Mamichita


class Chita(Base):
    def __init__(self):
        self.name = "Merime"
        self.surname = "Chitona"

        self.beauty = np.inf
        self.geniality = np.inf

        self.list_to_love = (Chito, Gatete, Pomtito, Mamichita)

        self.estado_civil = "chiteada"

    # Attributes
    def set_beauty(self, new_beauty):
        if new_beauty < np.inf:
            raise RuntimeError("Chita ech lo mach bonito que echiste")

        self.beauty = new_beauty

    def get_beauty(self, beauty):
        return self.beauty

    def set_geniality(self, new_geniality):
        if new_geniality < np.inf:
            raise RuntimeError("Chita ech lo mach genial que echiste")

        self.geniality = new_geniality

    def get_geniality(self, beauty):
        return self.geniality

    # Action methods
    def holi(self):
        """
        Says holi being muy mona
        """
        self.say("Holiiiii")

    def call_like_urraca(self):
        """
        Calls mamichita like an Urraca and mamichita receives the call

        :return: None
        """
        self.say("MAMAAAAAAAAAAAAAAAAAAAAA!!!!!!!!!!")
        self.mamichita.called_urraca()

    def empapelar_universidad(self):
        """
        One of her favourite activities. She wants to see the university burn
        """
        self.say("HIJOS DE PUTA!")

    # Reception methods
    def recibir_amor(self, other):
        if isinstance(other, self.list_to_love):
            self.say("AÑAÑA")


