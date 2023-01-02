import PySimpleGUI as sg
import click
sg.theme('dark')
layout = [
    [sg.Text("MDB 1 gui tool"), sg.Spin(["1","2"],key="spin")],
    [sg.Button("restart code")]
]

window=sg.Window("MDB 1", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "restart code":
        print(values)
window.close()