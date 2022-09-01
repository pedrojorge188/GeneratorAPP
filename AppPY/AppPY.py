from ast import Pass
import os
from distutils.command.clean import clean
import PySimpleGUI as app
from constants import *
import random
import string

Run = False
Passwords_List = []

app.theme("DarkAmber")

def restoreDb():
    with open('passwords.txt','r') as restore:

        line = restore.readline()

        if(line != ''):
            Passwords_List.append(line)

        while line != '':
            line = restore.readline()
            Passwords_List.append(line)

        

def savePassword(password):
      with open("passwords.txt",'a') as file:
                file.write(password+'\n')
      app.popup("Password Salva:")


def generatePassword(size):
    create = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + string.punctuation)
        for _ in range(size))
    return create


def initLayout(generatedPassword):

    layout = [[app.Text('Python Password Generator')],
              [app.Combo(['Pequena','Media', 'Grande'],readonly = True,text_color = 'white',default_value='Escolha o Tamanho...',key='selection',size=(20,1))],
              [app.Input(default_text=generatedPassword,readonly = True,text_color = 'black')],
              [app.Button("Generate")],
              [app.Button("Save Password")],
              [app.Button("Password Database")]]

    window = app.Window("Password Generation", layout)
    return window

def DBLayout():
    layout = [[app.Text('DataBase -> Saved Passwords')],[app.Text(text = '\n'+Passwords_List[data]+'\n', size = (30,40))                                     
                for data in range(len(Passwords_List))],
              [app.Button("Clear Database")]
             ]

    window = app.Window("DataBase", layout)
    return window

with open("passwords.txt",'a') as file:
            file.write('')

restoreDb()
while True:

    if Run == True:
        window.close()

    window = initLayout(password)
    Run = True
    event, values = window.read()

    if event == "Generate":
        if values['selection'] == 'Pequena':

            password = generatePassword(10)
            Passwords_List.append(password)

        elif values['selection'] == 'Media':

            password = generatePassword(20)
            Passwords_List.append(password)

        elif values['selection'] == 'Grande':

            password = generatePassword(50)
            Passwords_List.append(password)

        else:
            app.popup(PASSERROR)

    elif event == "Save Password":

        if password == DEFAULT:

            app.popup(PASSERROR)
        else:
            savePassword(password)

    elif event == 'Password Database':

        if Passwords_List != []:

            dataBaseWindow = DBLayout()
            e,v = dataBaseWindow.read()

            if e == "Clear Database":

                os.remove('passwords.txt')
                Passwords_List = []
                dataBaseWindow.close()
        else:
            app.popup(PASSERROR)

    elif event == app.WIN_CLOSED:

        break
       

window.close()