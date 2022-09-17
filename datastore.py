from user import User
from file_parser import FileParser


class Datastore:

    def __init__(self):
        self._users = []
        self.read_users()

    def read_users(self):
        file_parser = FileParser()
        self._users = file_parser.read_users("users.txt")

    def add_user(self, user):
        self._users.append(user)