# Task Manager CLI (Python)

A simple command-line task manager built with Python to practice object-oriented programming and data persistence using JSON.

This project allows users to create, view, complete, and delete tasks from a terminal-based menu. Tasks are stored in a JSON file so they persist between program executions.

---

## Features

* Add new tasks
* View all tasks
* Mark tasks as complete
* Delete completed tasks
* Tasks saved automatically in a JSON file
* Automatic task ID management

---

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* JSON for data storage
* Basic error handling

---

## Project Structure

```
project-folder/
│
├── main.py        # Program entry point and menu logic
├── task.py        # Task class definition
├── storage.py     # Functions to load and save tasks
└── tasks.json     # JSON file used to store tasks
```

---

## How to Run

1. Clone the repository

```
git clone https://github.com/yourusername/task-manager-python.git
```

2. Navigate to the project folder

```
cd task-manager-python
```

3. Run the program

```
python main.py
```

---

## Example Menu

```
-------------------
1. Add a task
2. See tasks
3. Complete task
4. Delete task
5. Exit
-------------------
```

Example output:

```

Tasker:
1. Study Python -> Incomplete
2. Go to the gym -> Complete

```

---

## What I Learned

While building this project I practiced:

* Writing and organizing Python classes
* Applying object-oriented programming concepts
* Reading and writing JSON files
* Managing data persistence between program runs
* Structuring a small Python project

---

## Possible Future Improvements

* Edit existing tasks
* Filter tasks (completed / incomplete)
* Add due dates or priorities
* Improve input validation

---

## Español

Pequeño gestor de tareas hecho en Python que funciona desde la terminal.

Permite:

* crear tareas
* ver la lista de tareas
* marcar tareas como completas
* eliminar tareas completadas

Las tareas se guardan en un archivo **JSON**, lo que permite que se mantengan entre ejecuciones del programa.
