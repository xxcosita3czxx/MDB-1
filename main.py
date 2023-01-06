#I DONT REALLY USE THIS TO RUN THE BOT, BETTER USE COMMAND "python3 src/bot.py"
#THIS COULD LAG YOUR ENTIRE COMP SO USE AT OWN RISK
import PySimpleGUI as sg
import click
import subprocess
import time
sg.theme('DarkAmber')
layout = [
    [sg.Text("MDB 1 gui tool")],
    [sg.Button("Start Code")]
]

window=sg.Window("MDB 1", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Start Code":
        subprocess.call("python src/bot.py", shell=True)
        while True:
            time.wait(0.5)
            window.refresh()
window.close()