# lab4
# Napisz manager contextu wspierający operacje na bazie danych w naszym przypadku sqllite
# https://docs.python.org/3/library/sqlite3.html
# /tests/context_manager/test_lab4.py

from contextlib import contextmanager
import sqlite3

class MyDBClass:

    def __init__(self, file_name):
        self.con = sqlite3.connect(file_name)
        self.cursor = self.con.cursor()


@contextmanager
def open_db(file_name: str):

    yield MyDBClass(file_name).cursor







