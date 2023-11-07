from user import User
from taskmanager import TaskManager

task_manager = TaskManager()
# print(dir(task_manager))

help = """
1) Regestrating
2) Log in
3) Add task
4) Sort task by due date
5) Today's task(s)
.* All by auto order
6) Delete task
7) Mark Af finished(✔)
"""
# username = input("Enter username: ")
run = True
while run:
    print(help)
    query = input("What's on your mind? ")
    match query:
        case 'q':
            run = False

        case '1':
            print("Here you are regestering yourself!")
            task_manager.register_user(input("Username: "),input("Email (example@gmial.com): "), input("Password: "))
            # print(task_manager.register_user())

        case '2':

            print("Logging in")
            user = task_manager.login_user(input("Enter your email please(example@gmial.com): "), input("Password: "))
            print(user)

        case '3':
            print("Add your task here")
            task_manager.add_task(user, input("Task: "), input("Description: "), input("Date: (2023-11-23)"))
            # print(task_manager.add_task())

        case '4':
            print("Sort tasks by due date")
            task_manager.sort_by_due_date(user)
            # print(task_manager.sort_by_due_date)
        
        case '5':
            print("Here today's tasks")
            today_tasks = task_manager.get_today_tasks(input("Username: "))
            print(today_tasks)
        case '.*':
            print("Here you are regestering yourself!")
            task_manager.register_user(input("Username: "),input("Email (example@gmial.com): "), input("Password: "))
            # print(task_manager.register_user())

            print("Logging in")
            user = task_manager.login_user(input("Enter your email please(example@gmial.com): "), input("Password: "))
            # print(user)

            print("Add your task here")
            task_manager.add_task(input("Task: "), input("Description: "), input("Date: (2023-11-23)"))
            # print(task_manager.add_task())

            print("Sort tasks by due date")
            # task_manager.sort_by_due_date(user)
            # print(today_tasks)

            print("Here today's tasks")
            today_tasks = task_manager.get_today_tasks(input("Username"))
            print(today_tasks)
        case '6':
            task_manager.delete_task(input("Username: "), int(input("Enter index of task you want to delete: ")))
            # print(task_manager.delete_task())
        case '7':
            task_manager.mark_as_completed(user, input('Enter index of task you want mark: '))