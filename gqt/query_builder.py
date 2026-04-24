import curses
import os
import sys
import textwrap
from contextlib import contextmanager
from dataclasses import dataclass
from graphql.language import parse
from .database import read_tree_from_database
from .database import write_tree_to_database
from .endpoint import fetch_schema
from .screen import addstr
from .screen import move
from .tree import Tree
from .tree import load_tree_from_schema
HELP_TEXT = 'Move:              <Left>, <Right>, <Up> and <Down>\n                   <Page-Up> and <Page-Down>\n                   <Meta-<> and <Meta->>\n                   <Tab>\nSelect:            <Space>\nVariable:          v\nDelete list item:  <Backspace>\nExecute:           <Enter>\nReload schema:     r\nHelp:              h or ?\nQuit:              q'
HELP_NCOLS = 55
COLOR_GRAY = 8

class QuitError(Exception):
    pass

def help_text():
    pass

@dataclass
class Title:
    kind: str
    tree: Tree
    description: str

class QueryBuilder:

    def __init__(self, stdscr, endpoint, query_name, headers, verify, variables):
        self.stdscr = stdscr
        self.endpoint = endpoint
        self.query_name = query_name
        self.headers = headers
        self.verify = verify
        self.variables = variables
        if self.variables:
            self.maximum_variable_length = max((len(variable) for variable in self.variables))
        else:
            self.maximum_variable_length = 0
        self.show_help = False
        self.y_offset = 1
        self.error = None
        self.meta = False
        self.show_description = False
        try:
            self.tree = read_tree_from_database(endpoint, query_name)
            self.show_fetching_schema = False
        except Exception:
            self.tree = None
            self.show_fetching_schema = True

    def draw(self, cursor, y_max, x_max, y):
        pass

    def update_key(self, key):
        pass

    def update_key_help(self, key):
        pass

    def update(self, key):
        pass

    def draw_fetching_schema(self):
        pass

    def draw_help(self):
        pass

    def draw_selector(self):
        pass

    def draw_variables(self, x_max):
        pass

    def run(self):
        pass

    def write_tree_to_database(self):
        pass

    def addstr(self, y, x, text):
        pass

    def addstr_frame(self, y, x, text):
        pass

    def addstr_error(self, y, x, text):
        pass

    def draw_title(self, y, title):
        pass

    def page_up_down_lines(self):
        pass

def format_description(description, maximum_width):
    pass

def selector(stdscr, endpoint, query_name, headers, verify, variables):
    pass

@contextmanager
def redirect_stdout_to_stderr():
    pass

def query_builder(endpoint, query_name, headers, verify, variables):
    pass
