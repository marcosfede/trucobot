import random


class Brain:

    def play(self, board, jugadas_disponibles):
        pass


class RandomBrain(Brain):
    def play(self, board, jugadas_disponibles):
        return random.choice(jugadas_disponibles)
