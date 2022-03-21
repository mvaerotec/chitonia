import numpy as np
from datetime import time

from base import Base
from gatete import Gatete
from chito import Chito
from pomtito import Pomtito
from mamichita import Mamichita
from .utils import *


class Chita(Base):
    def __init__(self):
        self.name = "Merime"

        self.beauty = np.inf
        self.geniality = np.inf

        self.siesta_init = time(16,30)
        self.siesta_end = time(17,30)

        self.siesta = check_time(self.siesta_init, self.siesta_end)

        self.list_to_love = (Chito, Gatete, Pomtito, Mamichita)

        self.estado_civil = "chiteada"

        self.available_actions = {
            "Amar": self.amar,
            "Llamar cual urraca": self.call_like_urraca,
            "Empapelar": self.empapelar,
            "Cambiar belleza": self.set_beauty,
            "Cambiar genialidad": self.set_geniality
        ]

    # Overriden methods
    def hello(self):
        self.holi()

    # Attributes
    def set_beauty(self, new_beauty):
        if new_beauty < np.inf:
            raise RuntimeError("Chita ech lo mach bonito que echiste, \
                               cholo che admite infinitibello")

        self.beauty = new_beauty

    def set_geniality(self, new_geniality):
        if new_geniality < np.inf:
            raise RuntimeError("Chita ech lo mach genial que echiste, \
                               cholo che admite infinitibello")

        self.geniality = new_geniality

    # Action methods
    def holi(self):
        """
        Says holi being muy mona
        """
        self.say("Holiiiii")

    def call_like_urraca(self, other):
        """
        Calls mamichita like an Urraca and mamichita receives the call

        :return: None
        """
        if isinstance(other, Mamichita):
            self.say("MAMAAAAAAAAAAAAAAAAAAAAA!!!!!!!!!!")
            other.called_urraca()

    def empapelar(self, who):
        """
        One of her favourite activities. She wants to see the university burn
        """
        if who != "universidad":
            self.say("Preferiría que fuese a la universidad, pero vale")
        else:
            self.say("Oh boy here we go again")
        self.say("HIJOS DE PUTA!")

    # Reception methods
    def recibir_amor(self, other):
        if isinstance(other, self.list_to_love):
            self.say("AÑAÑA")
        if isinstance(other, Chito):
            self.say("MIMICH BRBR")

    def no_love(self, other):
        self.say("Vete feo no che quien erech")

    def update(self):
        """
        Called after each loop, to update certain values

        In this case, we update siesta time
        """
        self.siesta = check_time(self.siesta_init, self.siesta_end)
