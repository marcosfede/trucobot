import brains


class Carta:
    def __init__(self, palo, numero):
        self.palo = palo
        self.numero = numero


class Game:
    def __init__(self, cartas, es_mano):
        self.cartas = [Carta(**carta) for carta in cartas]
        self.mano = es_mano
        self.puntos = 0
        self.puntos_oponente = 0
        self.tantos_oponente = None

    def add_score(self, puntos, puntos_oponente):
        self.puntos += puntos
        self.puntos_oponente += puntos_oponente

    def set_tantos_oponente(self, tantos):
        self.tantos_oponente = tantos


class FedeBot:

    def __init__(self):
        self.brain = brains.RandomBrain()

    def iniciar_mano(self, cartas, es_mano):
        self.game = Game(cartas, es_mano)

    def jugada_enemiga(self, jugada):
        pass

    def jugar(self, jugadas_disponibles):
        return self.brain.play(self.game, jugadas_disponibles)

    def resultado_mano(self, puntos, puntos_oponente):
        self.game.add_score(puntos, puntos_oponente)

    def resultado_partida(self, ganada):
        # analytics global
        pass

    def resultado_envido(self, ganado, tantos_oponente):
        # analytics local & global
        # analisis de cartas posibles del oponente
        self.game.set_tantos_oponente(tantos_oponente)
