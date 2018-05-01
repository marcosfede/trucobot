import json
import jugadas


def toJugadaInstance(jugada):
    if jugada["mensaje"] == "envido":
        return jugadas.Envido()
    elif jugada["mensaje"] == "real envido":
        return jugadas.RealEnvido()
    elif jugada["mensaje"] == "falta envido":
        return jugadas.FaltaEnvido()
    elif jugada["mensaje"] == "truco":
        return jugadas.Truco()
    elif jugada["mensaje"] == "retruco":
        return jugadas.ReTruco()
    elif jugada["mensaje"] == "vale 4":
        return jugadas.Vale4()
    elif jugada["mensaje"] == "carta":
        return jugadas.BajarCarta()
    elif jugada["mensaje"] == "quiero":
        return jugadas.Quiero()
    elif jugada["mensaje"] == "no quiero":
        return jugadas.NoQuiero()
    elif jugada["mensaje"] == "irse al mazo":
        return jugadas.IrseAlMazo()


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
        print(jugada)
        await self.ws.send(json.dumps(jugada.to_message()))

    async def resultadoMano(self, message):
        self.bot.resultado_mano(message["puntos"], message["puntosOponente"])

    async def resultadoPartida(self, message):
        self.bot.resultado_partida(message["ganada"])

    async def resultadoEnvido(self, message):
        self.bot.resultado_envido(message["ganado"], message["tantosOponente"])
