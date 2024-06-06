import PySimpleGUI as sg
from main import get_todos, write_todos, filepath

sg.theme('DarkBlue')

layout = [
    [sg.Text("Enter a new todo:"), sg.InputText(key='todo_input')],
    [sg.Button("Add"), sg.Button("Show"), sg.Button("Edit"), sg.Button("Complete"), sg.Button("Exit")],
    [sg.Listbox(values=[], size=(40, 10), key='todo_list', enable_events=True)],
    [sg.Text('', key='feedback', size=(40, 1))]
]

window = sg.Window("Todo List", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Add':
        todo = values['todo_input'].strip()
        if todo:
            todos = get_todos(filepath)
            todos.append(todo + '\n')
            write_todos(filepath, todos)
            window['todo_list'].update([todo.strip() for todo in todos])
            window['feedback'].update(f'Todo "{todo}" added.')
        else:
            window['feedback'].update("Cannot add an empty todo.")

    elif event == 'Show':
        todos = get_todos(filepath)
        if todos:
            window['todo_list'].update([todo.strip() for todo in todos])
            window['feedback'].update("Todos displayed.")
        else:
            window['feedback'].update("No todos to show.")

    elif event == 'Edit':
        try:
            selected_todo = values['todo_list'][0]
            new_todo = sg.popup_get_text('Enter a new todo', default_text=selected_todo).strip()
            if new_todo:
                todos = get_todos(filepath)
                index = todos.index(selected_todo + '\n')
                todos[index] = new_todo + '\n'
                write_todos(filepath, todos)
                window['todo_list'].update([todo.strip() for todo in todos])
                window['feedback'].update(f'Todo "{selected_todo}" has been updated to: {new_todo}')
            else:
                window['feedback'].update("Cannot update to an empty todo.")
        except IndexError:
            window['feedback'].update("Please select a todo to edit.")

    elif event == 'Complete':
        try:
            selected_todo = values['todo_list'][0]
            todos = get_todos(filepath)
            todos.remove(selected_todo + '\n')
            write_todos(filepath, todos)
            window['todo_list'].update([todo.strip() for todo in todos])
            window['feedback'].update(f'Todo "{selected_todo}" completed.')
        except IndexError:
            window['feedback'].update("Please select a todo to complete.")

window.close()
