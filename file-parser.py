from user import User

class File_Parser():

    def read_users(self, filename):
        users = []

        try:
            file = open(filename, "r")

            #file content stored in a list of strings
            lines = file.readlines()
            file.close()

        except IOError:
            print(f"Warning: Could not open {filename} for reading.")
            input("Return to continue")
            return users

        #loop through each line in file, parse & append users list
        for line in lines:
            user = self.parse_user_text(line)
            users.append(user)

        return users

    def parse_user_text(self, user_text):
        item = user_text.split(("|"))

        acc_num = item[0]
        f_name = item[1]
        l_name = item[2]
        seat_num = item[3]
        overdraft = item[4]
        token_bal = item[5]

        return User(acc_num, f_name, l_name, seat_num, overdraft, token_bal)

    def write_users(self, filename):
        lines = []

        try:
            file = open(filename, "w")
            file.writelines(lines)
            file.close()

        except IOError:
            print(f"Warning: Could not open {filename} for writing.")
            input("Return to continue")



    
       



