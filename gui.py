import functions
import PySimpleGUI as sg

layout = [[sg.Text('Type in a TO-DO')],
        [sg.InputText(key='todo'), sg.Button('Add')]]

window = sg.Window('My To-Do app', layout, font=('Ariel', 16))

while True:
        event, values = window.read()
        print(event)
        print(values)
        match event:
                case 'Add':
                        todos = functions.get_todos()
                        todos.append(values['todo'] + '\n')
                        functions.write_todos(todos)
                case sg.WINDOW_CLOSED:
                        break
window.close()
