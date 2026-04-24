import json
import shutil
from urllib.parse import quote_plus
from urllib.parse import unquote_plus
from xdg import XDG_DATA_HOME
from .tree import load_tree_from_json
DATABASE_PATH = XDG_DATA_HOME / 'gqt' / 'database'

def make_endpoint_path(endpoint):
    pass

def make_query_json_path(endpoint, query_name):
    pass

def make_most_recent_query_name_path(endpoint):
    pass

def read_tree_from_database(endpoint, query_name):
    pass

def write_tree_to_database(tree, endpoint, query_name):
    pass

def clear_database():
    pass

def get_queries():
    pass
