# Casa Inteligente - MQTT e CoAP Demo

Este projeto demonstra a integração de sensores ambientais e dispositivos de controle em uma casa inteligente usando os protocolos MQTT e CoAP.

## Arquitetura

- **Sensor Ambiental** (MQTT Publisher): Simula sensores que coletam dados de temperatura, umidade e luz.
- **Central de Controle** (MQTT Subscriber + CoAP Client): Processa dados dos sensores e controla dispositivos.
- **Termostato** (CoAP Server): Simula um dispositivo de controle de temperatura.

## Pré-requisitos

```bash
# Python 3.7+
python3 --version

# Pip para instalação de pacotes
pip --version
```

# Instalação

Clone o repositório e instale as dependências:

```bash
git clone
cd casa-inteligente-mqtt-coap
pip install paho-mqtt aiocoap
```

Inicie o serviço mosquitto

```bash
sudo systemctl start mosquitto
```

## Uso

No terminal 1 Inicie o Termostato

```bash
python3 termostato.py
```

Terminal 2 Inicie a Central de Controle

```bash
python3 central.py
```

Terminal 3 Inicie o Sensor Ambiental

```bash
python3 sensor.py
```

## Estrutura do projeto

```bash
.
├── README.md
├── central.py
├── sensor.py
└── termostato.py
```

# Funcionamento

- O sensor ambiental publica dados a cada 5 segundos via MQTT.
- A central de controle recebe os dados e verifica a temperatura.
- Se a temperatura exceder 25°C, a central envia um comando via CoAP para ligar o
