import numpy as np
from datetime import time

from .base import Base
from ..utils import *


class Chita(Base):
    """
    Chita is a chitonchita. She is the best, and I love her a lot. I'm going to
    eat her face.

    She likes doing Chita things, like empapelar cosas or calling like an
    urraca gente. She is a Chita.

    She also likes to play with Paichugato con forma
    """
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
            "Arreglar liada": self.arreglar_liada,
            "Alimentar": self.alimentar
        }

    # Overriden methods
    def hello(self):
        """
        Says holi being muy mona
        """
        self.say("Holiiiii")

    def action_possible(self):
        """
        In this case, action depends on whether it is siesta time or not.

        Chita is unavailable during siesta
        """
        if self.siesta:
            self.say("*Chita echta durmiendo la chiesta* dejame ma")
        return not self.siesta

    def update(self, alr_trig):
        """
        Called after each loop, to update certain values.
        In this case, we update siesta time
        """
        self.siesta = is_time_between(self.siesta_init, self.siesta_end)
        return False

    # Attributes
    def set_beauty(self, new_beauty):
        """
        Set chita's beauty. I wouldn't bother to try any value other than the
        real one...
        """
        if new_beauty < np.inf:
            raise RuntimeError("Chita ech lo mach bonito que echiste, " + \
                               "cholo che admite infinitibello")

        self.beauty = new_beauty

    def set_geniality(self, new_geniality):
        """
        Set chita's geniality. I wouldn't bother to try any value other than
        the real one...
        """
        if new_geniality < np.inf:
            raise RuntimeError("Chita ech lo mach genial que echiste," + \
                               "cholo che admite infinitibello")

        self.geniality = new_geniality

    # Action methods
    def call_like_urraca(self, other):
        """
        Calls `other` like an Urraca
        The behaviour depends on who is the other, but you can be sure that it
        will sound like an Urraca
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
        elif isinstance(other, __class__):
            self.say("CHITAAAAAAAAAAAAAAAA!!! Ah, si soy yo hehe")
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
        """
        Chita is the best when chito la ha liado. She sorts things out in
        this case
        """
        if chito.state == "liada" or chito.prev_state == "liada":
            self.say("A ver chiiiito que has hechoooo")
            chito.state = "felis"
            chito.prev_state = "felis"
            chito.say("Chita es la mejorchi ma")
        else:
            chito.say("Pero si año he hecho añadaaaaaa jo")

    # Reception methods
    def receive_love(self, other):
        """
        Chita likes to receive love, and behaviour depends on who is the one
        giving the love
        
        Important: do not give love during siesta, she is not going to like it
        """
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
            self.say("*Le ha arrancado la cabecha*")

    def no_love(self):
        """
        Chita does not like love from people she doesn't know. She sends him
        out, but in fact she ends up arrancandole la cabecha porque ech una
        chita
        """
        self.say("Vete feo no che quien erech")
        self.say("*Le ha arrancado la cabecha*")

    def alimentar(self, other):
        """
        We need to keep other players in game feeded. The behavior of the
        other depends on who it is. This method can be used to prevent
        losing due to gatete's hunger
        """
        from .gatete import Gatete
        from .pomtito import Pomtito
        from .chito import Chito

        if isinstance(other, Gatete):
            other.state = "averning"
            self.say("PEQUEÑO QUE TE HACE PAPI QUE NO TE DA DE COMER")
            other.say("*Comiendo triskitos*")
            other.maaaa()
        elif isinstance(other, Pomtito):
            self.say("Pomtito, cómete esto")
            other.say("*Lo huele*")
            other.say("Que te lo comas tuuuuuuu")
        elif isinstance(other, Chito):
            other.say("Cocholate")
            self.say("Yo querooooo")