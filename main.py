filepath = "todos.txt"

def get_todos(filepath):
    try:
        with open(filepath, "r") as file_local:
            todos_local = file_local.readlines()
    except FileNotFoundError:
        return []
    return todos_local

def write_todos(filepath, todos_arg):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    while True:
        user_action = input("Type add, show, edit, complete or exit: ").strip()

        if user_action.startswith('add'):
            todo = user_action[4:].strip()
            if todo:
                todos = get_todos(filepath)
                todos.append(todo + '\n')
                write_todos(filepath, todos)
                print(f'Todo "{todo}" added.')
            else:
                print("Cannot add an empty todo.")

        elif user_action.startswith('show'):
            todos = get_todos(filepath)
            if todos:
                print("Your todos:")
                for index, item in enumerate(todos, start=1):
                    item = item.strip('\n')
                    row = f"{index}-{item}"
                    print(row)
            else:
                print("No todos to show.")

        elif user_action.startswith('edit'):
            try:
                number = int(user_action[5:].strip())
                todos = get_todos(filepath)
                if 1 <= number <= len(todos):
                    new_todo = input("Enter a new todo: ").strip()
                    if new_todo:
                        todos[number - 1] = new_todo + '\n'
                        write_todos(filepath, todos)
                        print(f"Todo #{number} has been updated to: {new_todo}")
                    else:
                        print("Cannot update to an empty todo.")
                else:
                    print(f"Please enter a number between 1 and {len(todos)}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif user_action.startswith('complete'):
            try:
                number = int(user_action[9:].strip())
                todos = get_todos(filepath)
                if 1 <= number <= len(todos):
                    todo_to_remove = todos.pop(number - 1).strip('\n')
                    write_todos(filepath, todos)
                    print(f"Todo '{todo_to_remove}' completed.")
                else:
                    print(f"Please enter a number between 1 and {len(todos)}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except IndexError:
                print("Invalid input. Please enter a valid number.")

        elif user_action.startswith('exit'):
            print("Bye!")
            break

        else:
            print("Invalid input. Please type add, show, edit, complete, or exit.")
