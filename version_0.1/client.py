import asyncio
import websockets

async def send_message(websocket):
    message = input("Type a message to send to the server: ")
    await websocket.send(message)
    print(f"Sent: {message}")

async def receive_message(websocket):
    message = await websocket.recv()
    print(f"Received: {message}")

async def main():
    async with websockets.connect(uri) as websocket: 
        while True: # while connected to the server "app.py" await the following functions
            await send_message(websocket)
            await receive_message(websocket)

uri = input("what is the url: example 'ws://localhost:8765'")
asyncio.run(main())
