import functions
import PySimpleGUI as sg
import time

sg.theme('DarkPurple2')

layout = [[sg.Text('', key='time')],
        [sg.Text('Type in a TO-DO')],
         [sg.InputText(key='todo'), sg.Button('Add')],
         [sg.Listbox(values=functions.get_todos(), enable_events=True, size=(35, 10), key='todos'), sg.Button('Edit'), sg.Button('Complete')],
          [sg.Button('Exit')]]

window = sg.Window('My To-Do app', layout, font=('Ariel', 16))

while True:
        event, values = window.read(timeout=200)
        window['time'].update(value=time.strftime('%d-%b-%Y %H:%M:%S'))

        match event:
                case 'Add':
                        todos = functions.get_todos()
                        todos.append(values['todo'] + '\n')
                        functions.write_todos(todos)
                        window['todos'].update(values=todos)
                case 'Edit':
                        try:
                                todo_to_edit = values['todos'][0]
                                new_todo = values['todo']

                                todos = functions.get_todos()
                                index = todos.index(todo_to_edit)
                                todos[index] = new_todo

                                functions.write_todos(todos)
                                window['todos'].update(values=todos)
                        except IndexError:
                                sg.popup('Please select the item first')
                case 'Complete':
                        try:
                                todo_to_complete = values['todos'][0]

                                todos = functions.get_todos()
                                todos.remove(todo_to_complete)

                                functions.write_todos(todos)
                                window['todos'].update(values=todos)
                                window['todo'].update(value='')
                        except IndexError:
                                sg.popup('Please select the item first')
                case 'Exit':
                        break
                case 'todos':
                        window['todo'].update(value=values['todos'][0])

                case sg.WINDOW_CLOSED:
                        break
window.close()
