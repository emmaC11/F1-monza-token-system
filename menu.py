"""module providing menu prompts to user"""
import os
import random
from termcolor import colored, cprint
from user import User


class Menu():
    """'UI' of the system where users chooses action they want to take """

    def clear_terminal(self):
        os.system('clear')

    def validate_menu(self, ds):
        """Validates user input in display menu class
        to ensure selection is between 1-7"""
        user_input = "0"

        while user_input != "7":
            self.clear_terminal()
            user_input = self.display_menu(ds)

            if user_input not in ["1", "2", "3", "4", "5", "6", "7"]:
                print(f"Invalid menu option: {user_input}.")
                input("Press return to try again\n")

    def display_menu(self, ds):
        """displays menu options & calls functions based on users selection"""
        cprint("Welcome!", "magenta")
        cprint("Menu Options:", "magenta")
        print("1. View Current Users")
        print("2. Add User")
        print("3. Deposit Tokens")
        print("4. Withdraw Tokens")
        print("5. Transfer Tokens")
        print("6. Search for User")
        print("7. Exit Application")
        user_input = input("Please enter option (1-7):\n")

        if user_input == "1":
            self.view_users(ds)
        elif user_input == "2":
            self.add_user(ds)
        elif user_input == "3":
            self.add_tokens(ds)
        elif user_input == "4":
            self.withdraw_tokens(ds)
        elif user_input == "5":
            self.transfer_tokens(ds)
        elif user_input == "6":
            self.search_user(ds)
        elif user_input == "7":
            cprint("Thank you for using the F1 Monza Token System", "magenta")

        return user_input

    def view_users(self, ds):
        """displays all users in users.txt"""
        self.clear_terminal()
        cprint("Acc Number    First Name    Last Name    Seat Number    \
        Overdraft   Balance", "blue")

        for user in ds.users:
            print(user)
        input("Return to continue\n")

    def add_user(self, ds):
        """add user to the system"""
        self.clear_terminal()
        cprint("Add user to token system", "cyan")
        cprint("==========================", "cyan")

        valid = True

        # to do - generate acc number automatically
        while valid is True:
            first_name = input("First Name:\n ")
            last_name = input("Last Name:\n ")
            seat_num = input("Seat Number:\n ")

            print("Would you like to sign up to an overdraft facility?")
            print("Type 'y' to opt-in or 'n' to opt-out")
            overdraft = input("Overdraft: \n".lower())

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
                cprint(f"Invalid Overdraft Input: {overdraft}", "red")
                input("Return to continue\n")
                valid = False
                break

            elif first_name == "" or last_name == "" or seat_num == "":
                cprint("Fields cannot be left blank", "red")
                input("Return to continue\n")
                valid = False
                break

            elif valid_seat is False:
                print(f"Invalid Seat Number Input {seat_num}")
                cprint("Seat Number must include a number", "red")
                print("Return to continue")
                input()
                valid = False
                break

            new_user = User(
                first_name, last_name, seat_num, overdraft, balance)
            ds.add_user(new_user)
            cprint(f"new user {first_name} added successfully:", "green")
            input("Return to continue\n")
            valid = False

    def search_user(self, ds):
        """search for user in the system"""
        self.clear_terminal()
        cprint("Search for user:", "cyan")
        cprint("================", "cyan")

        acc_num = self.get_acc_num()

        acc_num_found = False

        for user in ds.users:
            if user.acc_num == acc_num:
                acc_num_found = True
                cprint(f"Account Number: {user.acc_num}  First Name:\
 {user.f_name} Seat Number: {user.seat_num}", "green")
                input("Press return to continue\n")

        if acc_num_found is False:
            cprint(f"Account Number '{acc_num}' cannot be found", "red")
            input("Press return to continue\n")

    def get_acc_num(self):
        """prompt user for account number & validate input"""
        acc_num_valid = False

        while acc_num_valid is False:
            try:
                acc_num = int(input("Please enter users account number: \n"))
            except ValueError:
                print("Invalid Account Number")
            else:
                acc_num_valid = True
        return acc_num

    def add_tokens(self, ds):
        """add tokens to users account"""
        self.clear_terminal()
        cprint("Add tokens to account", "cyan")
        cprint("=====================", "cyan")
        acc_num_found = False
        acc_num = self.get_acc_num()

        for user in ds.users:
            if user.acc_num == acc_num:

                acc_num_found = True
                cprint(f"Account Number: {user.acc_num}  First Name:\
 {user.f_name}  Last Name: {user.l_name}  Token Balance: {user.balance}", "green")

                new_token_balance = self.add_tokens_to_acc()

                if new_token_balance <= 0:
                    cprint("Token amount must be greater than 0", "red")
                    input("Return to continue\n")
                    break

                user.balance += new_token_balance

                cprint("Tokens added successfully!", "green")
                print(f"Account Number: {user.acc_num}  First Name:\
 {user.f_name}  Last Name: {user.l_name}  Token Balance: {user.balance}")
                input("Return to continue\n")

        if acc_num_found is False:
            cprint(f"Account Number '{acc_num}' cannot be found", "red")
            input("Press return to continue\n")

    def withdraw_tokens(self, ds):
        """withdraw tokens from users account"""
        self.clear_terminal()
        cprint("Withdraw tokens from account", "cyan")
        cprint("============================", "cyan")

        acc_num_found = False
        acc_num = self.get_acc_num()

        for user in ds.users:
            if user.acc_num == acc_num:
                acc_num_found = True
                cprint(f"Account Number: {user.acc_num}  First Name:\
 {user.f_name}  Last Name: {user.l_name}  Token Balance: {user.balance}", "green")

                new_token_balance = self.withdraw_tokens_from_acc()

                if user.balance < new_token_balance and user.overdraft == "n":
                    cprint("Insufficient number of tokens to withdraw.", "red")
                    cprint("You are not signed up to an overdraft facility", "red")
                    input("Press return to continue\n")
                    break
                elif user.balance == 0:
                    cprint("Cannot withdraw when token amount is 0", "red")
                    break
                elif new_token_balance <= 0:
                    cprint("Token amount to withdraw must be greater than 0", "red")
                    input("Press return to continue\n")
                    break

                user.balance -= new_token_balance
                code = self.token_code()

                cprint("Tokens withdrawn successfully!", "green")
                print(f"Account Number: {user.acc_num}  First Name:\
 {user.f_name}  Last Name: {user.l_name}  Token Balance: {user.balance}")
                cprint(f"Your token collection code is: {code}", "yellow")
                print("Enter this code at any of the token collection points\
 around the track to collect your tokens")
                input("Return to continue\n")

        if acc_num_found is False:
            print(f"Account Number '{acc_num}' cannot be found")
            input("Press return to continue\n")

    def withdraw_tokens_from_acc(self):
        """prompt user for withdraw amount & validate input"""
        token_balance_valid = False

        while token_balance_valid is False:
            try:
                withdraw_token = int(input("Enter amount of tokens to\
 withdraw: \n"))
            except ValueError:
                print("Token Balance must be a whole number")
            else:
                token_balance_valid = True

        return withdraw_token

    def token_code(self):
        """generates random string of numbers"""
        token_code = []

        for i in range(6):
            number = random.randint(1, 30)
            token_code.append(number)

        token_code = ' '.join(str(i) for i in token_code)
        return token_code

    def add_tokens_to_acc(self):
        """prompt user for token amount & validate input"""
        token_balance_valid = False

        while token_balance_valid is False:
            try:
                add_token = int(input("Enter amount of tokens to deposit: \n"))
            except ValueError:
                print("Token Balance must be a whole number")
            else:
                token_balance_valid = True

        return add_token

    def transfer_tokens(self, ds):
        """transfer tokens from one account number to another"""
        self.clear_terminal()
        cprint("Transfer tokens to another account", "cyan")
        cprint("==================================", "cyan")

        acc_num_found = False
        acc_num = self.get_acc_num()

        for user in ds.users:
            if user.acc_num == acc_num:

                acc_num_found = True

                cprint(f"Account Number: {user.acc_num}  First Name:\
 {user.f_name}  Last Name: {user.l_name}  Token Balance: {user.balance}", "green")

                token_transfer = self.token_transfer_amount()

                if user.overdraft == "n" and user.balance < token_transfer:
                    cprint("Cannot transfer tokens", "red")
                    cprint("You are not signed up to an overdraft facility", "red")
                    input("Return to continue")
                    break
                elif token_transfer <= 0:
                    cprint("Cannot transfer tokens", "red")
                    cprint("Transfer amount must be a whole positive number", "red")
                    input("Return to continue")
                    break
                elif user.balance == 0:
                    cprint("Cannot transfer tokens", "red")
                    cprint("Balance cannot be 0", "red")
                    input("Return to continue")
                    break

                user.balance -= token_transfer

                print("Enter account number of user you want to transfer\
 tokens to:")
                transfer_acc_num = self.transfer_acc_num()

                if acc_num == transfer_acc_num:
                    cprint("Cannot transfer tokens to same account number", "red")
                    input("Return to continue")
                    break

                for user in ds.users:
                    if user.acc_num == transfer_acc_num:
                        acc_num_found = True

                        user.balance += token_transfer
                        cprint(f"{token_transfer} tokens successfully\
 transfered to account number {transfer_acc_num}", "green")
                        input("Return to continue \n")

        if acc_num_found is False:
            print(f"Invalid account number: '{acc_num}'")
            input("Return to continue")

    def token_transfer_amount(self):
        """prompt user for transfer amount & validate input"""
        token_transfer_valid = False

        while token_transfer_valid is False:
            try:
                transfer_token = int(input("Enter amount of tokens to\
 transfer: \n"))
            except ValueError:
                print("Token Balance must be a whole number")
            else:
                token_transfer_valid = True

        return transfer_token

    def transfer_acc_num(self):
        """prompt user for transfer account number & validate input"""
        acc_num_valid = False

        while acc_num_valid is False:
            try:
                acc_num_transfer = int(input("Account Number to receive\
 tokens: \n"))
            except ValueError:
                print("Account Number must be a whole positive number")
            else:
                acc_num_valid = True

        return acc_num_transfer
