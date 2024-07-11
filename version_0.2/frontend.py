from tkinter import *
from backend import WebSocketServer
import asyncio

# Create an instance of WebSocketServer
localhost_port = 1432
server = WebSocketServer(localhost_port)

# Define the button click function to run the asyncio method
def button_click_localhost(e):
    port_value = e.get()
    asyncio.run(server.button_click_localhost(port_value))

# Start GUI
root = Tk()
root.title("Jack's Calculation")

e = Entry(root, width=25, borderwidth=5)
e.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

connect_to_localhost_button = Button(root, text="Submit", padx=40, pady=20, command=lambda: button_click_localhost(e))
connect_to_localhost_button.grid(row=0, column=0, columnspan=1, padx=1, pady=1)

root.mainloop()
