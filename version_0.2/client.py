# client.py
import asyncio
import websockets

async def connect_to_server(uri):
    try:
        async with websockets.connect(uri) as websocket:
            print("Connected to server")
            await websocket.send("Hello, Server!")
            response = await websocket.recv()
            print(f"Received: {response}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    uri = "ws://localhost:1234"  # Ensure this matches your server's address and port
    asyncio.run(connect_to_server(uri))
