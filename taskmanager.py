from signer import SignIn
from pathlib import Path

signin = SignIn()
cwd = Path.cwd()
"""
This class helps user to add, remove, sort
"""
class TaskManager:
    def __init__(self):
        self.title = ''
        self.description = ''
        self.due_date = ''
        self.completed = 'X'

    def new_task(self):
        self.title = input("Tasks title: ")
        self.description = input("Tasks Description")
        self.due_date = input("Du Date: (2023-11-23)")

    def task_adding(self):
        cwd = cwd / self.signin.username

        with open (f"{cwd}/{cwd}_tasks.txt", 'a') as file:
            file.write(f"{self.title}:{self.description}:{self.due_date}:{self.completed}")