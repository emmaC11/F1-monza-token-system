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

    
       



