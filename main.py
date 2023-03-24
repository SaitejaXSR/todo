import functions


while True:
    user_action = input('Enter add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{index + 1}-{todo}")

    elif user_action.startswith("edit"):
        try:
            index = int(user_action[5:])
            index = index - 1

            new_todo = input("Enter new todo to edit: ") + '\n'

            todos = functions.get_todos()
            todos[index] = new_todo

            functions.write_todos(todos)

        except ValueError:
            print('Wrong command, Please enter the number of todo with edit')
            continue
    elif user_action.startswith("complete"):
        try:
            index = int(user_action[9:])
            index = index - 1

            todos = functions.get_todos()
            completed_todo = todos[index].strip('\n')
            todos.pop(index)

            print(f"Todo {completed_todo} is completed and removed from the list")
            functions.write_todos(todos)
        except IndexError:
            print('Todo not present, please Try again!')
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid command, please Try again!!")
        continue
print("Bye!")