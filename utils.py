from data import *
from stats import *


def signup(username, full_name, password, email):
    usernames.append(username)
    passwords.append(password)
    fullnames.append(full_name)
    emails.append(email)


def login(username, password, email):
    login_stats.append(f"User: {username},Password:  {password},Email:  {email}")


def newTodo(Todo):
    todos.append(f"{Todo}, from user: {}")


def ask_admin():
    admin_wants == True

    while admin_wants == True:
        print('''
What do you want to do??
write the number 1 to go to settings
write the number 2 to go to menu''')
        print()

        menu_or_settings = int(input())

        if menu_or_settings == 1:
            print('''
write the number 1 to check how many todos are there for a specific user that you specify.
write the number 2 to check how many todos are there.
write the number 3 to check how many accounts are there in the database.
write q to quit.
    ''')

            menu = int(input(""))

            if menu == "q":
                break

            elif menu == 1:
                user = input("Enter the users name")

                todo_count = 0

                for i in range(len(todos)):
                    if user in todos[i]:
                        todo_count += 1
                    else:
                        todo_count = todo_count
                # answer
                print(f"Here is the counted number of todos for the specified user {todo_count}")

            elif menu == 2:
                print(f"In total there are {len(todos)} todos")

            elif menu == 3:
                print(f"In total there are {len(accounts)} accounts")
            else:
                continue

        elif menu_or_settings == 2:
            print('''
write the number 1 to check how much money that you have gotten from users.
write q to quit''')

            settings = int(input(""))

            if settings == "q":
                break

            elif settings == 1:
                print(f"This is how much money that you have earned: {moneyEarned}")

            else:
                break
