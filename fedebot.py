import brains
import jugadas


class Carta:
    def __init__(self, palo, numero):
        self.palo = palo
        self.numero = numero

    def __repr__(self):
        return f'Carta: {self.numero} de {self.palo}'

    def __eq__(self, other):
        self.palo == other.palo and self.numero == other.numero


class Hand:
    def __init__(self, cartas, es_mano):
        self.cartas_en_mano = [Carta(**carta) for carta in cartas]
        self.cartas_en_mesa = []
        self.cartas_en_mesa_oponente = []
        self.mano = es_mano
        self.tantos_oponente = None

    def set_tantos_oponente(self, tantos):
        self.tantos_oponente = tantos

    def bajar_carta(self, carta):
        self.cartas_en_mano.remove(carta)
        self.cartas_en_mesa.append(carta)

    def bajar_carta_oponente(self, carta):
        self.cartas_en_mesa_oponente.append(carta)


class Game:
    def __init__(self):
        self.puntos = 0
        self.puntos_oponente = 0

    def add_score(self, puntos, puntos_oponente):
        self.puntos += puntos
        self.puntos_oponente += puntos_oponente


class FedeBot:

    def __init__(self):
        self.brain = brains.RandomBrain()
        self.game = Game()

    def iniciar_mano(self, cartas, es_mano):
        self.hand = Hand(cartas, es_mano)

    def jugada_enemiga(self, jugada):
        if isinstance(jugada, jugadas.BajarCarta):
            self.hand.bajar_carta_oponente(jugada.carta)

    def jugar(self, jugadas_disponibles):
        jugada = self.brain.play(self.hand, jugadas_disponibles)
        if isinstance(jugada, jugadas.BajarCarta):
            self.hand.bajar_carta(jugada.carta)
        return jugada

    def resultado_mano(self, puntos, puntos_oponente):
        self.game.add_score(puntos, puntos_oponente)

    def resultado_partida(self, ganada):
        # analytics global
        self.game = Game()

    def resultado_envido(self, ganado, tantos_oponente):
        # analytics local & global
        # analisis de cartas posibles del oponente
        self.hand.set_tantos_oponente(tantos_oponente)
