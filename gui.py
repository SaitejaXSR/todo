import functions
import PySimpleGUI as gui

label = gui.Text("Type in a todo")
input_box = gui.InputText(tooltip="Enter a todo", key='todo')
add_button = gui.Button("Add")


window = gui.Window("To-Do App",
                    layout=[[label], [input_box], [add_button]],
                    font=('Mukta', 14))

while True:
    event, values = window.read()
    print(event)
    print(values)
    window['todo'].update(value=values['todos'][0].strip())
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case gui.WIN_CLOSED:
            break


window.close()