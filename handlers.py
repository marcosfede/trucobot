import json
from jugadas import Jugada


def toJugadaInstance(jugada):
    return Jugada.toInstance(jugada["mensaje"])


class MessageHandler:
    def __init__(self, bot, websocket):
        self.bot = bot
        self.ws = websocket

    async def iniciarMano(self, message):
        self.bot.iniciar_mano(message["cartas"], message["esMano"])

    async def pedirJugada(self, message):
        self.bot.jugada_enemiga(toJugadaInstance(message["jugadaAnterior"]))
        jugadas_disponibles = [toJugadaInstance(
            jugada) for jugada in message["jugadasDisponibles"]]
        jugada = self.bot.jugar(jugadas_disponibles)
        print('>>>',jugada)
        await self.ws.send(json.dumps(jugada.to_message()))

    async def resultadoMano(self, message):
        self.bot.resultado_mano(message["puntos"], message["puntosOponente"])

    async def resultadoPartida(self, message):
        self.bot.resultado_partida(message["ganada"])

    async def resultadoEnvido(self, message):
        self.bot.resultado_envido(message["ganado"], message["tantosOponente"])
