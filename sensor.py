import paho.mqtt.client as mqtt
import random
import time
import json

BROKER = 'localhost'
TOPIC = 'casa/sensor'
CLIENT_ID = 'sensor'

def generate_sensor_data():
    """Gera dados simulados de temperatura, umidade e luz."""
    temperatura = round(random.uniform(20.0, 30.0), 2)
    umidade = round(random.uniform(30.0, 70.0), 2)
    luz = random.choice(["claro", "escuro"])
    return {
        "temperatura": temperatura,
        "umidade": umidade,
        "luz": luz
    }

def main():
    client = mqtt.Client(client_id=CLIENT_ID, callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
    client.connect(BROKER)
    
    while True:
        data = generate_sensor_data()
        # Convertendo o dicionário para JSON string antes de publicar
        json_data = json.dumps(data)
        client.publish(TOPIC, json_data)
        print(f"Publicado: {data}")
        time.sleep(1)

if __name__ == "__main__":
    main()