from user import User

class TaskManager:
    # def __init__(self, username):
    #     self.username = register_user()
    username = ''
    def register_user(self, username_, email, password):
        with open(f'{username_}.txt', 'a') as file:
            file.write(f"{email},{password}\n")
            self.username = username_
    

    def login_user(self, email, password):
        with open(f'{self.username}.txt', 'r') as file:
            for line in file:
                user_info = line.split(',')
                if user_info[0] == email and user_info[1] == password:
                    return User(email, password)
        return "Email or password is incorrect. Try again!"

    def add_task(self, title, description, due_date):
        with open(f'{self.username}_tasks.txt', 'a') as file:
            file.write(f"{title},{description},{due_date},False\n")

    def delete_task(self, username, task_index):
        with open(f'{username}_tasks.txt', 'r') as file:
            tasks = file.readlines()
        with open(f'{username}_tasks.txt', 'w') as file:
            for i, task in enumerate(tasks):
                if i == task_index:
                    file.write(task)

    def mark_as_completed(self, task_index):
        with open(f'{self.username}_tasks.txt', 'r') as file:
            tasks = file.readlines()
        tasks[task_index] = tasks[task_index].replace('False', 'True')
        with open(f'{self.username}_tasks.txt', 'w') as file:
            for task in tasks:
                file.write(task)

    def sort_by_due_date(self):
        with open(f'{self.username}_tasks.txt', 'r') as file:
            tasks = file.readlines()
        tasks.sort(key=lambda x: x.split(',')[3])
        with open(f'{self.username}_tasks.txt', 'w') as file:
            for task in tasks:
                file.write(task)

    def get_today_tasks(self, filename):
        today_tasks = []
        with open(f'{filename}_tasks.txt', 'r') as file:
            print(file.readlines())
            # for line in file:
                # task_info = line.split(',')
                # if task_info[3] == 'today':
                # today_tasks.append(line)
        # return today_tasks