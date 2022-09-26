# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
"""file that runs the program, calls datastore & menu module"""
from datastore import Datastore
from menu import Menu

ds = Datastore()
menu = Menu()

menu.validate_menu(ds)
