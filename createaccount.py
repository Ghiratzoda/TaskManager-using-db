import pathlib



CWD = pathlib.Path.cwd()
# from helper import create_dir
"""
This class allowes user create account if he/she doesn not have an account.
"""

class CreateAccount:
    def __init__(self):
        self.username = ''
        self.email = ''
        self.password = ''
        self.path_email_password = ''
        self.path_user_tasks = ''

    def create_account(self):
        self.username = input("Username: ")
        self.email = input("Email: ")
        self.password = input("Password: ")
        self.data_saving()


    def data_saving(self):
        new_folder = self.username
        new_dir = CWD / new_folder
        if not new_dir.exists():
            new_dir.mkdir(parents=True)
        else:
            print(f"{new_folder} username exists. Try another username")

        with open(f'{new_dir}/{self.username}.txt', 'w') as file:
            file.write(f"{self.email}:{self.password} \n")
            self.path_email_password = f"{new_dir}/{self.username}.txt"
        with open(f'{new_dir}/{self.username}_tasks.txt', 'w') as file:
            file.write('')
            self.path_user_tasks = f"{new_dir}/{self.username}_tasks.txt"

        

