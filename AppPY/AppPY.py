import PySimpleGUI as app
from constants import *
import random
import string

CheckBox = [app.Checkbox(text = '',default = 'Pequeno')]
GenerateButton = [app.Button("Generate")]

def generatePassword():
    create = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) 
        for _ in range(MAX_SIZE))
    return create


def initLayout(generatedPassword):
    layout = [[app.Text(generatedPassword)],CheckBox, GenerateButton]
    window = app.Window("Password Generation", layout ,size=(500, 250))
    return window

while True:
    window = initLayout(password)
    event, values = window.read()

    if event == "Generate":
        password = generatePassword()
    elif event == app.WIN_CLOSED:
        break
       

window.close()