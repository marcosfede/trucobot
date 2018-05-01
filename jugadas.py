class Jugada:

    def __str__(self):
        return str(self.to_message())


class Truco(Jugada):

    def to_message(self):
        return {
            "mensaje": "truco"
        }


class ReTruco(Jugada):

    def to_message(self):
        return {
            "mensaje": "retruco"
        }


class Vale4(Jugada):

    def to_message(self):
        return {
            "mensaje": "vale 4"
        }


class Envido(Jugada):
    def to_message(self):
        return {
            "mensaje": "envido"
        }


class RealEnvido(Jugada):
    def to_message(self):
        return {
            "mensaje": "real envido"
        }


class FaltaEnvido(Jugada):
    def to_message(self):
        return {
            "mensaje": "falta envido"
        }


class Quiero(Jugada):
    def to_message(self):
        return {
            "mensaje": "quiero"
        }


class NoQuiero(Jugada):
    def to_message(self):
        return {
            "mensaje": "no quiero"
        }


class BajarCarta(Jugada):
    def __init__(self, carta=None):
        self.carta = carta

    def to_message(self):
        return {
            "mensaje": "carta",
            "carta": {
                "palo": self.carta.palo,
                "numero": self.carta.numero
            }
        }


class IrseAlMazo(Jugada):
    def to_message(self):
        return {
            "mensaje": "irse al mazo"
        }
