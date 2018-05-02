import random
import jugadas
random.seed(0)


class Brain:

    def play(self, hand, jugadas_disponibles):
        pass


class RandomBrain(Brain):
    def play(self, hand, jugadas_disponibles):
        choice = random.choice(jugadas_disponibles)
        if isinstance(choice, jugadas.BajarCarta):
            carta = random.choice(hand.cartas_en_mano)
            return jugadas.BajarCarta(carta)
        return choice
