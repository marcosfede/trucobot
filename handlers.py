import json


class MessageHandler:
    def __init__(self, bot, websocket):
        self.bot = bot
        self.ws = websocket

    async def iniciarMano(self, message):
        self.bot.iniciar_mano(message["cartas"], message["esMano"])

    async def pedirJugada(self, message):
        self.bot.jugada_enemiga(message["jugadaAnteriorOponente"])
        jugada = self.bot.jugar(message["jugadasDisponibles"])
        await self.ws.send(json.dumps(jugada))

    async def resultadoMano(self, message):
        self.bot.resultado_mano(message["puntos"], message["puntosOponente"])

    async def resultadoPartida(self, message):
        self.bot.resultado_partida(message["ganada"])

    async def resultadoEnvido(self, message):
        self.bot.resultado_envido(message["ganado"], message["tantosOponente"])
