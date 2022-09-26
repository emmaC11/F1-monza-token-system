"""module that reads & writes data from users.txt"""


from file_parser import FileParser


class Datastore:
    """ class that calls the file parser to read users & can add users """

    def __init__(self):
        self._users = []
        self.read_users()

    def read_users(self):
        """ creates instance of file parser object and reads users.txt file """
        file_parser = FileParser()
        self._users = file_parser.read_users("users.txt")

    def add_user(self, user):
        """appends user list with a new user"""
        self._users.append(user)

    @property
    def users(self):
        """getter for users list"""
        return self._users
