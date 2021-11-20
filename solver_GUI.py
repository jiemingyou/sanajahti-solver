from sanajahti import Game
import PySimpleGUI as sg


def f():
    words = set()
    with open("kotus_wordlist.txt") as f:
        for word in f:
            word = word.strip()
            words.add(word)

    letters = ""
    for v in range(4):
        for u in range(4):
            letters += values[str(v)+str(u)]
    letters = list(letters)
    game = Game(letters, words)
    lst = game.solve()
    return lst

txt = ("Arial", 16)
txt2 = ("Arial", 14)
layout = [[sg.Text('Please enter the letters', font=txt )],
          [sg.InputText(font=txt2,key='00',size=(5,5)), sg.InputText(font=txt2,key='01',size=(5, 5)), sg.InputText(font=txt2,key='02',size=(5, 5)), sg.InputText(font=txt2,key='03',size=(5, 5))],
          [sg.InputText(font=txt2,key='10',size=(5, 5)), sg.InputText(font=txt2,key='11',size=(5, 5)), sg.InputText(font=txt2,key='12',size=(5, 5)), sg.InputText(font=txt2,key='13',size=(5, 5))],
          [sg.InputText(font=txt2, key='20',size=(5, 5)), sg.InputText(font=txt2,key='21',size=(5, 5)), sg.InputText(font=txt2,key='22',size=(5, 5)), sg.InputText(font=txt2,key='23',size=(5, 5))],
          [sg.InputText(font=txt2, key='30',size=(5, 5)), sg.InputText(font=txt2,key='31',size=(5, 5)), sg.InputText(font=txt2,key='32',size=(5, 5)), sg.InputText(font=txt2,key='33',size=(5, 5))],
          [sg.Button('Find', font=txt), sg.Button('Stop', font=txt)],
          [sg.Output(size=(100,200), key='-OUTPUT-', font=txt2)]
          ]

window = sg.Window('Sanajahti solver v1.0', layout, size=(400, 600))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Stop':
        break

    if event == 'Find':
        answer = f()
        for word in answer:
            print(word)

    else:
        print('User cancelled')