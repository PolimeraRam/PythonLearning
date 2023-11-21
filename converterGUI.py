import PySimpleGUI as sg
from PySimpleGUI \
    import WIN_CLOSED

import functions

lable1 = sg.Text("Enter Feet: ")
feets = sg.Input(key="feets_key")
lable2 = sg.Text("Enter inches: ")
inches = sg.Input(key="inches_key")
convertButton = sg.Button("Convert", key="convert_key")

resultLabel = sg.Text(key="result-key")

w = sg.Window("Converter", layout=[[lable1], [feets], [lable2], [inches],[convertButton], [resultLabel]])

while True:
    event, values = w.read()
    if event == "convert_key":
        f = float(values["feets_key"])
        i = float(values["inches_key"])
        m = functions.convert_feetinches_to_meters(feets=f, inches=i)
        w["result-key"].update(m)
    elif event == WIN_CLOSED:
        break

w.close()

