from tkinter import simpledialog
import requests as r
import tkinter as tk
import hashlib as h
import json as j
import sys

global username
global password
username = ""
password = ""
def construct_request_json(request, parameters):
    rq = {}
    rq["request"] = request
    keys = list(parameters.keys())
    values = list(parameters.values())
    kv = []
    for i in range(len(keys)):
        kv.append({"key": keys[i], "value": values[i]})
    rq["parameters"] = kv
    return rq

win = tk.Tk()
win.title("Prism Chat Client (Alpha v0.0.1)")
win.geometry("250x500")
win.withdraw()
global address
address = simpledialog.askstring(title="Prism Chat", prompt="Enter the server address")
if not address:
    win.destroy()
    sys.exit(0)
win.deiconify()

global auth_token
auth_token = None

uname = tk.Entry(win)
uname.place(x=0, y=0, relwidth=1)
passw = tk.Entry(win)
passw.place(x=0, y=30, relwidth=1)
loginb = tk.Button(win, text="Login")
loginb.place(x=0, y=60, relwidth=0.3)
chat = tk.Label(win, text="Log in to chat!")
chat.place(x=0, y=80, relwidth=1, height=380)
textinput = tk.Entry(win)
textinput.place(relx=1, rely=1, relwidth=1, anchor="se")
textinput.insert(0, "Send a message")
def login(uname, passw):
    log = r.post("", json=j.dumps(construct_request_json("login", {"username": uname, "passwordHash": h.sha1(passw)}))).json()
    rs = log["success"]
    if rs:
        username = uname
        password = passw
    auth_token = log["token"]
    

win.mainloop()