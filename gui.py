import functions
import PySimpleGUI

label = PySimpleGUI.Text('Type in a TO-DO')
input_box = PySimpleGUI.InputText()
add_button = PySimpleGUI.Button('Add')

window = PySimpleGUI.Window('My To-Do app', layout=[[label], [input_box, add_button]])
window.read()