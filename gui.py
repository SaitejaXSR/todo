import functions
import PySimpleGUI as gui
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass
clock = gui.Text(key="clock")
window_font = ('Helvetica', 12)
button_font = ('Calibri', 10)
label = gui.Text("Type in a todo")
input_box = gui.InputText(tooltip="Enter a todo", key='todo')
add_button = gui.Button("Add", font=button_font)
list_box = gui.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=(45, 10))
edit_button = gui.Button("Edit", font=button_font)
complete_button = gui.Button("Complete", font=button_font)
exit_button = gui.Button("Exit", font=button_font)

window = gui.Window("To-Do App",
                    layout=[[clock], [label], [input_box],
                            [add_button, edit_button, complete_button],
                            [list_box], [exit_button]],
                    font=window_font)

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime('%d %b, %Y %H:%M:%S'))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                gui.popup("Select a todo to edit!")
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                gui.popup("Please select a todo to complete!")
                continue
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0].strip())
        case gui.WIN_CLOSED:
            break


window.close()