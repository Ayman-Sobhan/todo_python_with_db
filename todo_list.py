from utils import *
import usernames.csv
from stats import *
import pandas as pd

admin = "Acga89892012"

admin_username = None
admin_password = None

logged_into_admin = False

account_yes_no = input(
    "Do you have an account for the terminal todo app (y/n)> ")
if account_yes_no == "y" or account_yes_no == "Y":
    username_input_for_login = input("What is your account username > ")
    password_input_for_login = input("What is your account password > ")
    email_input_for_login = input("What is your email ")

    # to input it to the data.py's login_stats and login in utils.py

    login(username_input_for_login,
          password_input_for_login, email_input_for_login)
    login_stats.append(
        f"User: {username_input_for_login}, Password: {password_input_for_login}, Email: {email_input_for_login}")

elif account_yes_no == admin:
    ask_for_admin_username = input("Enter the username for admin > ")
    ask_for_admin_password = input("Enter the password for admin > ")

    admin_username = ask_for_admin_username
    admin_password = ask_for_admin_password

    logged_into_admin = True

else:
    print("We'll make sure that all of you're info(information) stays secret now please fill in the form below")

    ask_for_username = input(
        "Since you don't have an account let's get you started! Enter you're new username > ")
    ask_for_password = input(
        "For your account you need a password. So enter your password right here > ")
    ask_for_first_name = input(
        "We'll also need you're first name so write it right here > ")
    ask_for_second_name = input(
        "Everyone has a second name so right it here > ")
    ask_for_third_name = input(
        "Write your third name if you have one if write any word or character like n,N,No,NO,nO or anything like that > ")

    donation_ask = input("We'd really appreciate if you donated even a dollar (y/n) > ")
    donation_ask = donation_ask.lower()

    if donation_ask == "y":
        how_to_donate = int(input('''
1. Visa
2. Mastercard
3. Premier bank
4. Paypal'''))

        if how_to_donate == 1:
            Card_num = int(input("Enter your card number > "))
            money = int(input("How much money do you want to donate (in dollar) > "))
        elif how_to_donate == 2:
            Card_num = int(input("Enter your card number > "))
            money = int(input("How much money do you want to donate (in dollar) > "))
        elif how_to_donate == 3:
            Card_num = int(input("Enter your card number > "))
            money = int(input("How much money do you want to donate (in dollar) > "))
        else:
            Card_num = int(input("Enter your card number > "))
            money = int(input("How much money do you want to donate (in dollar) > "))
    moneyEarned = moneyEarned + money

    ask_for_third_name = ask_for_third_name.lower()

    if ask_for_third_name == "n" or ask_for_third_name == "no":
        ask_for_third_name = None
    else:
        ask_for_third_name = ask_for_third_name


todoAsk = input("Do you want a new todo (y/n) > ")
todoAsk = todoAsk.lower()

todoGetAsk = False

if todoAsk == "y":
    todoGet = input("Enter the todo > ")
    newTodo(todoGet)
    user_wanted_todo = input("Enter you're user name > ")

    todoWantAsk = input("Do you want to see all of your todos (y/n) > ")

    if todoWantAsk == "y":
        todoGetAsk = True
    else:
        todoGetAsk = False

# admin stuffRefactor

nothing = True

if logged_into_admin == True:
    ask_admin()
else:
    nothing = False

#
# # this is the database for the todolist app #
#
# usernames = []
# passwords = []
# firstnames = []
# secondnames = []
# thirdnames = []
# emails = []
#
# login_stats = []
#
# # account todos #
#
# todos = []
pd..
