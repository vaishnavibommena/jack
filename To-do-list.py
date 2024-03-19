class Task:
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):
        return f'Task ID: {self.id}, Title: {self.title}, Description: {self.description}, Completed: {self.completed}'

# Example of creating a task
example_task = Task(1, 'Learn Python', 'Complete the Python course on Julius AI.', False)
print(example_task)

tasks = []

def add_task(id, title, description):
    new_task = Task(id, title, description)
    tasks.append(new_task)
    print(f'Task added: {new_task}')

def view_tasks():
    for task in tasks:
        print(task)

# Adding a couple of tasks for demonstration
add_task(1, 'Learn Python', 'Complete the Python course on Julius AI.')
add_task(2, 'Grocery Shopping', 'Buy milk, bread, and eggs.')

# Viewing the added tasks
print('Current Tasks:')
view_tasks()

def display_menu():
    print('To-Do List Application')
    print('1. Add Task')
    print('2. View Tasks')
    print('3. Update Task')
    print('4. Delete Task')
    print('5. Mark Task as Completed')
    print('6. Exit')

# Display the menu
print('Welcome to the To-Do List Application')
display_menu()