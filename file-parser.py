from user import User

class File_Parser():

    def read_users(self, filename):
        users = []

        try:
            file = open(filename, "read")

            #file content stored in a list of strings
            lines = file.readlines()
            file.close()

       



