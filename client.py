import asyncio
import websockets
import json

iniciar_mano = {
    "mensaje": "iniciarMano",
    "cartas": [
        {
            "palo": "oro",
            "numero": 1
        },
        {
            "palo": "basto",
            "numero": 7
        },
        {
            "palo": "espada",
            "numero": 3
        },
    ],
    "esMano": True
}

pedir_jugada = {
    "mensaje": "pedirJugada",
    "jugadaAnterior": {
        "mensaje": "carta",
        "carta": {
            "palo": "basto",
            "numero": 4
        }
    },
    "jugadasDisponibles": [
        {
            "mensaje": "envido",
            "carta": None
        },
        {
            "mensaje": "truco",
            "carta": None
        },
        {
            "mensaje": "irse al mazo",
            "carta": None
        }

    ]
}


async def hello():
    async with websockets.connect('ws://localhost:3000') as ws:
        await ws.send(json.dumps(iniciar_mano))
        await ws.send(json.dumps(pedir_jugada))
        greeting = await ws.recv()
        print("< {}".format(greeting))

asyncio.get_event_loop().run_until_complete(hello())
