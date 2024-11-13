import paho.mqtt.client as mqtt
import asyncio
import aiocoap
from aiocoap import Message, Code
import json

BROKER = 'localhost'
MQTT_TOPIC = 'casa/sensor'
CLIENT_ID = 'central_de_controle'
COAP_SERVER = 'coap://localhost/termostato'

def process_sensor_data(data):
    """Processa os dados do sensor e verifica se o termostato deve ser acionado."""
    temperatura = data.get('temperatura')
    if temperatura and temperatura > 25.0:
        print("Temperatura alta detectada. Enviando comando para o Termostato...")
        asyncio.run(send_coap_command())

async def send_coap_command():
    """Envia um comando CoAP para o Termostato."""
    context = await aiocoap.Context.create_client_context()
    request = Message(code=Code.POST, payload=b"ON")
    request.set_request_uri(COAP_SERVER)
    response = await context.request(request).response
    print(f"Resposta do Termostato: {response.payload.decode()}")

def on_message(client, userdata, message):
    data = json.loads(message.payload.decode())
    print(f"Dados recebidos: {data}")
    process_sensor_data(data)

def main():
    client = mqtt.Client(client_id=CLIENT_ID, callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
    client.on_message = on_message
    client.connect(BROKER)
    client.subscribe(MQTT_TOPIC)
    
    print("Central de Controle iniciada...")
    client.loop_forever()

if __name__ == "__main__":
    main()