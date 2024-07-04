import asyncio
import websockets
from tkinter import *


# button logic
localhost_port = int
def button_click_localhost(number):
    localhost_port = e.get()
    print(type(localhost_port))
    print(localhost_port)

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


print("the version of Tkinter is...", TkVersion)
# start GUI
root = Tk()
root.title("jacks calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
connect_to_localhost_button = Button(root, text="submit", padx=40, pady=20, command=lambda: button_click_localhost(1)) # the button cmd number
connect_to_localhost_button.grid(row=0, column=0, columnspan=1, padx=1, pady=1)

root.mainloop() # end tinker

start_server = websockets.serve(handler, "localhost", localhost_port)

print("Server started")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()



