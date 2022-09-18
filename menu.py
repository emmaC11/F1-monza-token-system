from user import User
from file_parser import FileParser


class Menu():

    def display_menu(self, ds):
        print("Welcome!")
        print("Menu Options:")
        print("1. View Current Users")
        print("2. Add User")
        print("3. Deposit Tokens")
        print("4. Withdraw Tokens")
        print("5. Transfer Tokens")
        print("6. Search for User")
        print("7. Help")
        print("8. Exit Application")

        user_input = 0

        if user_input == "1":
            print("call to view users function")
        elif user_input == "2":
            print("call to add user function")
        elif user_input == "3":
            print("call to deposit function")
        elif user_input == "4":
            print("call to withdraw function")
        elif user_input == "5":
            print("call to transfer function")
        elif user_input == "6":
            print("call to search function")
        elif user_input == "7":
            print("call to help function")
        elif user_input == "8":
            print("exit application")

    def view_users(self, ds):
        print("Acc Number    First Name    Last Name    Seat Number    Overdraft   Balance")
        print("===========================================================================")

        for user in ds.users:
            print(user)

        
            
