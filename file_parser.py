"""module that parses content from the txt file"""

from user import User


class FileParser:
    """ class that parses data from the users.txt file """

    def read_users(self, filename):
        """ function that reads data from a file """

        users = []

        try:
            file = open(filename, "r", encoding="utf-8")

            # file content stored in a list of strings
            lines = file.readlines()
            file.close()

        except IOError:
            print(f"Warning: Could not open {filename} for reading.")
            input("Return to continue")
            return users

        # loop through each line in file, parse & append users list
        for line in lines:
            user = self.parse_user_text(line)
            users.append(user)

        return users

    def parse_user_text(self, user_text):
        """ function that parses text content & returns user object """

        item = user_text.split(("|"))

        f_name = item[1]
        l_name = item[2]
        seat_num = item[3]
        overdraft = item[4]
        token_bal = item[5]

        return User(f_name, l_name, seat_num, overdraft, token_bal)

    def write_users(self, filename):
        """ function that writes data to a file """

        lines = []

        try:
            file = open(filename, "w", encoding="utf-8")
            file.writelines(lines)
            file.close()

        except IOError:
            print(f"Warning: Could not open {filename} for writing.")
            input("Return to continue")
