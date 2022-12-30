import PySimpleGUI as sg

layout = [
    [sg.Text("MDB 1 gui tool"), sg.Spin(["1","2"])],
    [sg.Button("restart code")],
    [sg.Input()]
]

window=sg.Window("MDB 1", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "restart code":
        print("Restart Code")
window.close()