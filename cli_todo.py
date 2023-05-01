from functions import get_todos, write_todos
import time

prompt = "Type add, show, edit, complete or exit: "

print('It is',time.strftime('%b %d, %Y %H:%M:%S'))

while True:
    user_action = input(prompt)
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = get_todos()
        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos, start=1):
            print(f"{index}-{item}".strip('\n'))

    elif user_action.startswith('edit'):
        try:
            numer = int(user_action[5:]) - 1

            todos = get_todos()

            todos[numer] = input("Edit: ") + '\n'

            write_todos(todos)

        except ValueError:
            print('invalid command.')

    elif user_action.startswith('exit'):
        break

    elif user_action.startswith('complete'):
        try:
            numer = int(user_action[9:]) - 1

            todos = get_todos()

            todos.pop(numer)

            write_todos(todos) 

        except ValueError:
            print('Wrong format - add numer of completed task')
        except IndexError:
            print('Index out of range')

    else:
        print('Command is unknown')
print('Bye!')
