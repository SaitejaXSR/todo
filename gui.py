import functions
import PySimpleGUI as gui

label = gui.Text("Type in a todo")
input_box = gui.InputText(tooltip="Enter a todo", key='todo')
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=[45, 10])
edit_button = gui.Button("Edit")

window = gui.Window("To-Do App", layout=[[label], [input_box], [add_button, edit_button], [list_box]], font=('Mukta', 14))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0].strip())
        case gui.WIN_CLOSED:
            break


window.close()