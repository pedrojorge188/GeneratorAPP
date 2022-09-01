from distutils.command.clean import clean
import PySimpleGUI as app
from constants import *
import random
import string

Run = False

app.theme("DarkAmber")

def generatePassword(size):
    create = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + string.punctuation)
        for _ in range(size))
    return create


def initLayout(generatedPassword):

    layout = [[app.Text('Python Password Generator')],
              [app.Combo(['Pequena','Media', 'Grande'],readonly = True,text_color = 'white',default_value='Escolha o Tamanho...',key='selection',size=(20,1))],
              [app.Input(default_text=generatedPassword,readonly = True,text_color = 'black')],
              [app.Button("Generate")]]

    window = app.Window("Password Generation", layout)

    return window

while True:

    if Run == True:
        window.close()

    window = initLayout(password)
    Run = True
    event, values = window.read()

    if event == "Generate":
        if values['selection'] == 'Pequena':
            password = generatePassword(10)
        elif values['selection'] == 'Media':
            password = generatePassword(20)
        elif values['selection'] == 'Grande':
            password = generatePassword(50)
        else:
            app.popup("Introuza o tamanho da password")
    elif event == app.WIN_CLOSED:
        break
       

window.close()