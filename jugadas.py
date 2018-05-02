class Jugada:

    @classmethod
    def toInstance(cls, mensaje):
        for subclass in cls.__subclasses__():
            if subclass.mensaje == mensaje:
                return subclass()
        raise RuntimeError()

    def __str__(self):
        return str(self.to_message())

    def to_message(self):
        return {
            "mensaje": self.mensaje
        }


class Null(Jugada):
    mensaje = ""


class Truco(Jugada):
    mensaje = "truco"


class ReTruco(Jugada):
    mensaje = "retruco"


class Vale4(Jugada):
    mensaje = "vale 4"


class Envido(Jugada):
    mensaje = "envido"


class RealEnvido(Jugada):
    mensaje = "real envido"


class FaltaEnvido(Jugada):
    mensaje = "falta envido"


class Quiero(Jugada):
    mensaje = "quiero"


class NoQuiero(Jugada):
    mensaje = "no quiero"


class BajarCarta(Jugada):
    mensaje = "carta"

    def __init__(self, carta=None):
        self.carta = carta

    def to_message(self):
        return {
            "mensaje": self.mensaje,
            "carta": {
                "palo": self.carta.palo,
                "numero": self.carta.numero
            }
        }


class IrseAlMazo(Jugada):
    mensaje = "irse al mazo"
