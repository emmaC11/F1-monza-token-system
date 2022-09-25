from user import User
from file_parser import FileParser
import random


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
            self.add_tokens(ds)
        elif user_input == "4":
            print("call to withdraw function")
            self.withdraw_tokens(ds)
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
            if user.acc_num == acc_num:

                acc_num_found = True
                print(f"Account Number: {user.acc_num}  First Name: {user.f_name}  Last Name: {user.l_name}  Token Balance: {user.balance}")

                new_token_balance = self.add_tokens_to_acc()

                if(new_token_balance <= 0):
                    print("Token amount must be greater than 0")
                    input("Return to continue")
                    break

                user.balance += new_token_balance 

                print("Tokens added successfully!")
                print(f"Account Number: {user.acc_num}  First Name: {user.f_name}  Last Name: {user.l_name}  Token Balance: {user.balance}")
                input("Return to continue")


        if acc_num_found is False:
            print(f"Account Number '{acc_num}' cannot be found")
            input("Press return to continue")

    def withdraw_tokens(self, ds):
        print("Withdraw tokens from account")
        print("============================")

        acc_num_found = False
        acc_num = self.get_acc_num()

        for user in ds.users:
            if user.acc_num == acc_num:
                acc_num_found = True
                print(f"Account Number: {user.acc_num}  First Name: {user.f_name}  Last Name: {user.l_name}  Token Balance: {user.balance}")

                new_token_balance = self.withdraw_tokens_from_acc()

                if user.balance < new_token_balance and user.overdraft == "n":
                    print("Insufficient number of tokens to withdraw.\n You are not signed up to an overdraft facility")
                    input("Press return to continue")
                    break
                elif user.balance == 0:
                    print("Cannot withdraw when token amount is 0")
                    break
                elif new_token_balance <= 0:
                    print("Token amount to withdraw must be greater than 0")
                    input("Press return to continue")
                    break

                user.balance -= new_token_balance
                code = self.token_code()

                print("Tokens withdrawn successfully!")
                print(f"Account Number: {user.acc_num}  First Name: {user.f_name}  Last Name: {user.l_name}  Token Balance: {user.balance}")
                print(f"Your token collection code is: {code}")
                print("Enter this code at any of the token collection points around the track to collect your tokens")
                input("Return to continue")

                

    def withdraw_tokens_from_acc(self):
        token_balance_valid = False

        while token_balance_valid is False:
            try:
                withdraw_token = int(input("Enter amount of tokens to withdraw: "))
            except ValueError:
                print("Token Balance must be a whole number")
            else:
                token_balance_valid = True

        return withdraw_token

    def token_code(self):
        token_code = []

        for i in range(6):
            number = random.randint(1, 30)
            token_code.append(number)

        token_code = ' '.join(str(i) for i in token_code)
        return token_code









        
    def add_tokens_to_acc(self):
        token_balance_valid = False

        while token_balance_valid is False:
            try:
                add_token = int(input("Enter amount of tokens to deposit: "))
            except ValueError:
                print("Token Balance must be a whole number")
            else:
                token_balance_valid = True

        return add_token

    
    def transfer_tokens(self, ds):
        print("Transfer tokens to another account")
        print("==================================")

        acc_num_found = False
        acc_num = self.get_acc_num()

        for user in ds.users:
            if user.acc_num == acc_num
            acc_num_found = True

            print(f"Account Number: {user.acc_num}  First Name: {user.f_name}  Last Name: {user.l_name}  Token Balance: {user.balance}")

            token_transfer = self.token_transfer_amount()

    def token_transfer_amount(self):
        token_transfer_valid = False

        while token_transfer_valid is False:
            try:
                transfer_token = int(input("Enter amount of tokens to transfer: "))
            except ValueError:
                print("Token Balance must be a whole number")
            else:
                token_transfer_valid = True

        return transfer_token

    def transfer_acc_num(self):
        acc_num_valid = False

        while acc_num_valid is False:
            try:
                acc_num_transfer = int(input("Account Number to receive tokens: "))
            except ValueError:
                print("Account Number must be a whole positive number")
            else:
                acc_num_valid = True
                
        return acc_num_transfer



