import pathlib
from createaccount import CreateAccount
from  signer import SignIn

print(pathlib.Path.cwd())

signin = SignIn()
accounting = CreateAccount()
run = True
while run:
    print("1) Sing in")
    print("2) Create account")
    query = input("What's on your mind? ")
    match query:
        case '1':
            print(query)
            signin.sign_in()
        case '2':
            accounting.create_account()
        case 'q':
            run = False