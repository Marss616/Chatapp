import asyncio
import websockets
from frontend import *
from backend import *

connected = set()

localhost_port = 1432


start_server = websockets.serve(handler, "localhost", localhost_port)

print("Server started")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()



