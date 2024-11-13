import asyncio
from aiocoap import resource, Context, Message, Code
import time

class ThermostatResource(resource.Resource):
    def __init__(self):
        super().__init__()
        self.state = "OFF"
        self.last_on_time = None
        self.timeout = 10  # tempo em segundos para desligar automaticamente

    async def check_state(self):
        """Verifica periodicamente se deve desligar o termostato"""
        while True:
            if self.state == "ON" and self.last_on_time:
                if time.time() - self.last_on_time > self.timeout:
                    self.state = "OFF"
                    print(f"Termostato desligado automaticamente após {self.timeout} segundos")
            await asyncio.sleep(1)

    async def render_post(self, request):
        """Recebe comandos para alterar o estado do Termostato."""
        payload = request.payload.decode()
        self.state = payload
        if payload == "ON":
            self.last_on_time = time.time()
        print(f"Termostato ajustado para: {self.state}")
        return Message(payload=f"Termostato {self.state}".encode())

async def main():
    # Criar o recurso
    thermostat = ThermostatResource()
    
    # Configurar o site
    root = resource.Site()
    root.add_resource(['termostato'], thermostat)

    # Iniciar o servidor
    await Context.create_server_context(root)
    
    # Iniciar a verificação periódica do estado
    asyncio.create_task(thermostat.check_state())
    
    print("Termostato iniciado...")
    
    # Manter o servidor rodando
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())