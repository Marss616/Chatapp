import asyncio
import websockets

class WebSocketServer:
    def __init__(self, localhost_port):
        self.localhost_port = localhost_port
        self.connected = set()

    async def button_click_localhost(self, port_value):
        self.localhost_port = int(port_value)
        print(type(self.localhost_port))
        print(self.localhost_port)

    async def send_message(self, websocket):
        message = await asyncio.get_event_loop().run_in_executor(None, input, "Enter message: ")
        await websocket.send(message)
        print(f"Sent: {message}")

    async def receive_message(self, websocket):
        message = await websocket.recv()
        print(f"Received: {message}")

    async def handler(self, websocket, path):
        self.connected.add(websocket)
        print("A client connected")
        try:
            while True:
                await self.receive_message(websocket)
                await self.send_message(websocket)
        except websockets.ConnectionClosedOK:
            pass
        finally:
            self.connected.remove(websocket)
            print("A client disconnected")
