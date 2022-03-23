import numpy as np
from datetime import time

from .base import Base
from ..utils import *


class Chita(Base):
    def __init__(self):
        self.name = "Merime"

        self.state = "chiteante"

        self.beauty = np.inf
        self.geniality = np.inf

        self.siesta_init = time(16,30)
        self.siesta_end = time(17,30)

        self.siesta = is_time_between(self.siesta_init, self.siesta_end)

        # Importing inside init to avoid circular import
        from .gatete import Gatete
        from .pomtito import Pomtito
        from .chito import Chito
        from .mamichita import Mamichita
        self.list_love = (Chito, Gatete, Pomtito, Mamichita)

        self.estado_civil = "chiteada"

        self.available_actions = {
            "Amar": self.love,
            "Llamar cual urraca": self.call_like_urraca,
            "Empapelar": self.empapelar,
            "Cambiar belleza": self.set_beauty,
            "Cambiar genialidad": self.set_geniality,
            "Arreglar liada": self.arreglar_liada
        }

    # Overriden methods
    def hello(self):
        """
        Says holi being muy mona
        """
        self.say("Holiiiii")

    def action_possible(self):
        if self.siesta:
            self.say("*Chita echta durmiendo la chiesta* dejame ma")
        return not self.siesta

    def update(self):
        """
        Called after each loop, to update certain values

        In this case, we update siesta time
        """
        self.siesta = is_time_between(self.siesta_init, self.siesta_end)

    # Attributes
    def set_beauty(self, new_beauty):
        if new_beauty < np.inf:
            raise RuntimeError("Chita ech lo mach bonito que echiste, " + \
                               "cholo che admite infinitibello")

        self.beauty = new_beauty

    def set_geniality(self, new_geniality):
        if new_geniality < np.inf:
            raise RuntimeError("Chita ech lo mach genial que echiste," + \
                               "cholo che admite infinitibello")

        self.geniality = new_geniality

    # Action methods
    def call_like_urraca(self, other):
        """
        Calls mamichita like an Urraca and mamichita receives the call

        :return: None
        """
        from .mamichita import Mamichita
        from .chito import Chito
        from .gatete import Gatete
        from .pomtito import Pomtito
        if isinstance(other, Mamichita):
            self.say("MAMAAAAAAAAAAAAAAAAAAAAA!!!!!!!!!!")
            other.called_urraca()
        elif isinstance(other, Chito):
            self.say("CHITOOOOOOOOOOO!!!!!!!!!!!!")
        elif isinstance(other, Gatete):
            self.say("GATETEEEEEEEEEEEEEEEEEEEE!!!!!!!!!!!!")
        elif isinstance(other, Pomtito):
            self.say("Pomki deja de comerte al SEÑOOOOOOOOR!!!!!!!!!!!!")
        else:
            self.say("TUUUUUUUUUUUUUUUUUUUUUUUUU!!!!!!!!")

    def empapelar(self, who):
        """
        One of her favourite activities. She wants to see the university burn
        """
        if who != "universidad":
            self.say("Preferiría que fuese a la universidad, pero vale")
        else:
            self.say("Oh boy here we go again")
        self.say("HIJOS DE PUTA!")

    def arreglar_liada(self, chito):
        if chito.state == "liada":
            self.say("A ver chiiiito que has hechoooo")
            chito.state = "felis"
            chito.say("Chita es la mejorchi ma")
        else:
            chito.say("Pero si año he hecho añadaaaaaa jo")

    # Reception methods
    def receive_love(self, other):
        if self.siesta:
            self.say("Dejame que echtoy dormididor")
            return
        from .chito import Chito
        from .mamichita import Mamichita
        if isinstance(other, Chito):
            self.say("MIMICH BRBR")
        elif isinstance(other, Mamichita):
            self.say("Mamiiiiiii")
        elif isinstance(other, self.list_love):
            self.say("AÑAÑA")
        else:
            self.say("Vete feo no che quien erech")

    def no_love(self):
        self.say("Vete feo no che quien erech")
