import functions
import PySimpleGUI as sg

layout = [[sg.Text('Type in a TO-DO')],
        [sg.InputText(key='todo'), sg.Button('Add')],
        [sg.Listbox(values=functions.get_todos(), enable_events=True, size=(45, 10), key='todos'), sg.Button('Edit')]]

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
                        window['todos'].update(values=todos)
                case 'Edit':
                        todo_to_edit = values['todos'][0]
                        new_todo = values['todo']

                        todos = functions.get_todos()
                        index = todos.index(todo_to_edit)
                        todos[index] = new_todo

                        functions.write_todos(todos)
                        window['todos'].update(values=todos)
                case 'todos':
                        window['todo'].update(value=values['todos'][0])

                case sg.WINDOW_CLOSED:
                        break
window.close()
