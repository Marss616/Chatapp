# backend.py
import asyncio
import websockets

class WebSocketServer:
    def __init__(self, port):
        self.port = port

    async def handle_connection(self, websocket, path):
        async for message in websocket:
            await websocket.send(message)  # Echo back the received message

    async def start(self):
        server = await websockets.serve(self.handle_connection, "localhost", self.port)
        print(f"Server started on ws://localhost:{self.port}")
        await server.wait_closed()  # Keep the server running

def run_server(port):
    server = WebSocketServer(port)
    print(f"Starting server on ws://localhost:{port}")
    asyncio.run(server.start())
    print("Server stopped")
