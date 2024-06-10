import asyncio
import websockets

async def send_message(websocket):
    message = await asyncio.get_event_loop().run_in_executor(None, input, "Type a message to send to the client: ")
    await websocket.send(message)
    print(f"Sent: {message}")

async def receive_message(websocket):
    message = await websocket.recv()
    print(f"Received: {message}")

async def handler(websocket, path):
    # Register.
    connected.add(websocket)
    print("A client connected")
    try:
        while True:
            await receive_message(websocket)
            await send_message(websocket)
    except websockets.ConnectionClosedOK:
        pass
    except websockets.ConnectionClosedError:
        pass
    finally:
        # Unregister when client disconnects.
        connected.remove(websocket)
        print("A client disconnected")

connected = set()

start_server = websockets.serve(handler, "localhost", 8765)
print("Server started")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
