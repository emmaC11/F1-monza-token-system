from user import User
from file_parser import FileParser


class Menu():

    def validate_menu(self, ds):
        user_input = "0"

        while (user_input != "8"):
            user_input = self.display_menu(ds)
           
            if user_input not in ["1","2","3","4","5","6","7","8"]:
                print(f"Invalid menu option: {user_input}. Press return to try again")
                input()

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
        user_input = input("Please enter option (1-8)")

        if user_input == "1":
            print("call to view users function")
            self.view_users(ds)
        elif user_input == "2":
            print("call to add user function")
            self.add_user(ds)
        elif user_input == "3":
            print("call to deposit function")
        elif user_input == "4":
            print("call to withdraw function")
        elif user_input == "5":
            print("call to transfer function")
        elif user_input == "6":
            print("call to search function")
            self.search_user(ds)
        elif user_input == "7":
            print("call to help function")
        elif user_input == "8":
            print("exit application")
        
        return user_input

    def view_users(self, ds):
        print("Acc Number    First Name    Last Name    Seat Number    Overdraft   Balance")
        print("===========================================================================")

        for user in ds.users:
            print(user)

    def add_user(self, ds):
        print("Add user to token system")
        print("==========================")

        valid = True
        
        # to do - generate acc number automatically
        while valid is True:
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            seat_num = input("Seat Number: ")
            
            print("Would you like to sign up to an overdraft facility?\n Type 'y' to opt-in or 'n' to opt-out")
            overdraft = input("Overdraft: ".lower())

            # charge of 10 tokens for overdraft facility
            if overdraft == "y":
                balance = 10
            else:
                balance = 20

            for char in seat_num:
                if char.isdigit():
                    valid_seat = True
                else:
                    valid_seat = False

            # validation
            if overdraft != "y" and overdraft != "n":
                print(f"Invalid Overdraft Input: {overdraft}")
                print("Return to continue")
                input()
                valid = False
                break
                
            elif first_name == "" or last_name == "" or seat_num == "":
                print("Fields cannot be left blank")
                print("Return to continue")
                input()
                valid = False
                break

            elif valid_seat is False:
                print(f"Invalid Seat Number Input {seat_num}")
                print("Seat Number must include a number")
                print("Return to continue")
                input()
                valid = False
                break

                    
            new_user = User(first_name, last_name, seat_num, overdraft, balance)
            ds.add_user(new_user)
            print(f"new user {first_name} added successfully:")
            print("Return to continue")
            input()
            valid = False

    def search_user(self, ds):
        print("Search for user:")
        print("================")

        acc_num = self.get_acc_num()

        acc_num_found = False

        for user in ds.users:
            if user.acc_num == acc_num:
                acc_num_found = True
                print(f"Account Number: {user.acc_num}  First Name: {user.f_name}  Seat Number: {user.seat_num}")
                input("Press return to continue")

        if acc_num_found is False:
            print(f"Account Number '{acc_num}' cannot be found")
            input("Press return to continue")

    def get_acc_num(self):
        acc_num_valid = False

        while acc_num_valid is False:
            try:
                acc_num = int(input("Please enter users account number: "))
            except ValueError:
                print("Invalid Account Number")
            else:
                acc_num_valid = True
        return acc_num

    def add_tokens(self, ds):
        print("Add tokens to account")
        print("=====================")
        acc_num_found = False
        acc_num = self.get_acc_num()

        for user in ds.users:
            if user.acc_num = acc_num
            acc_num_found = True

