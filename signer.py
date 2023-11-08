import pathlib
from createaccount import CreateAccount
# from signer import SignIn
# from taskmanager import TaskManager
import os

# task_manager = TaskManager()
accounting = CreateAccount()
CWD = pathlib.Path.cwd()

class SignIn:
    def __init__(self):
        self.username = ''

    def sign_in(self):
        self.username = input("Enter username: ")

        list_of_items = [] # Here are items which exists in cwd dir
        for item in os.listdir(CWD):
            list_of_items.append(item)

        if self.username in list_of_items:
            print("===================== You are in ========================")
            # task_manager.new_task()
        else:
            print("Error: Username is incorrect. Try again.")