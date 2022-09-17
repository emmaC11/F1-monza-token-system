from user import User
from file_parser import FileParser


class Datastore:

    def __init__(self):
        self._users = []
        self.read_users()