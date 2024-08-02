# frontend.py
from tkinter import *
import threading
from backend import run_server

def start_server_thread(port):
    threading.Thread(target=run_server, args=(port,), daemon=True).start()

def button_click_localhost():
    port_value = int(e.get())
    start_server_thread(port_value)
    root.quit()  # Exit the Tkinter application

def start_gui():
    global root, e
    root = Tk()
    root.title("Jack's Chat-App")

    e = Entry(root, width=25, borderwidth=5)
    e.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

    connect_to_localhost_button = Button(root, text="Submit", padx=40, pady=20, command=button_click_localhost)
    connect_to_localhost_button.grid(row=0, column=0, columnspan=1, padx=1, pady=1)

    root.mainloop()
