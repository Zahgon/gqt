import curses
from readlike import edit
from .screen import addstr
KEY_BINDINGS = {'KEY_BACKSPACE': 'backspace', '\x08': 'backspace', 'KEY_DC': 'backspace', '\x7f': 'backspace', '\x01': 'ctrl a', '\x04': 'ctrl d', '\x05': 'ctrl e', '\x0b': 'ctrl k', '\x14': 'ctrl t', 'KEY_LEFT': 'left', '\x1b\x7f': 'meta backspace', '\x1bKEY_BACKSPACE': 'meta backspace', '\x1bd': 'meta d', 'kLFT5': 'meta left', 'kRIT5': 'meta right', 'KEY_RIGHT': 'right'}
OPTIONAL_SYMBOLS = {'â–¡': 'â–\xa0', 'â–\xa0': 'â–¡'}

def is_optional_argument(field_type):
    pass

def has_default(default_value):
    pass

class QueryError(Exception):

    def __init__(self, message, node):
        super().__init__()
        self.message = message
        self.node = node

class Value:

    def __init__(self):
        self.text = ''
        self.pos = 0

    def edit(self, key):
        pass

def query_variable(value, value_type, variables, node):
    pass

def make_field_name_attrs(is_deprecated):
    pass

def find_root_field(cursor):
    pass

def is_field_implementor(offset, implementors_offset):
    pass

def fields_query(fields, variables, is_union=False, implementors_offset=None):
    pass

def create_fields_from_possible_types(possible_types, types):
    pass

class Cursor:

    def __init__(self):
        self.node = None
        self.y = 0
        self.x = 0
        self.y_mutation = None

class Node:

    def __init__(self):
        self.parent = None
        self.child = None
        self.next = None
        self.prev = None
        self.type = None
        self.description = None

    def draw(self, stdscr, y, x, cursor, is_implementor=False):
        pass

    def key_left(self):
        pass

    def key_right(self):
        pass

    def select(self):
        pass

    def key(self, _key):
        pass

    def query(self, variables):
        pass

    def is_selected(self):
        pass

    def to_json(self, cursor):
        pass

    def from_json(self, data):
        pass

class Object(Node):

    def __init__(self, name, field_type, description, fields, state, number_of_query_fields, is_root=False, is_union=False, is_deprecated=False, number_of_implementors=0):
        super().__init__()
        self.name = name
        self.type = field_type
        self.description = description
        self.fields = fields
        self.state = state
        self.is_deprecated = is_deprecated
        if not is_root:
            self.fields.parent = self
        self.is_root = is_root
        self.is_union = is_union
        self.number_of_query_fields = number_of_query_fields
        self.is_expanded = is_root
        self._name_attrs = None
        if number_of_implementors == 0:
            self.implementors_offset = None
        else:
            self.implementors_offset = len(fields) - number_of_implementors

    def name_attrs(self):
        pass

    def draw(self, stdscr, y, x, cursor, is_implementor=False):
        pass

    def query(self, variables):
        pass

    def key_left(self):
        pass

    def key_right(self):
        pass

    def query_root(self, cursor):
        pass

    def select(self):
        pass

    def is_selected(self):
        pass

    def to_json(self, cursor):
        pass

    def from_json(self, data):
        pass

class Leaf(Node):

    def __init__(self, name, field_type, description, fields, state, is_deprecated):
        super().__init__()
        self._is_selected = False
        self.name = name
        self.type = field_type
        self.description = description
        self.fields = fields
        self.state = state
        self.is_deprecated = is_deprecated
        self._name_attrs = None
        if self.fields is not None:
            self.fields.parent = self

    def name_attrs(self):
        pass

    def draw(self, stdscr, y, x, cursor, is_implementor=False):
        pass

    def draw_with_arguments(self, stdscr, y, x, cursor):
        pass

    def draw_without_arguments(self, stdscr, y, x, cursor):
        pass

    def select(self):
        pass

    def query(self, variables):
        pass

    def is_selected(self):
        pass

    def to_json(self, cursor):
        pass

    def from_json(self, data):
        pass

class ScalarArgument(Node):

    def __init__(self, name, field_type, description, default_value, state, types):
        super().__init__()
        self.name = name
        self._type = get_type(field_type)['name']
        self.type = get_type_string(field_type)
        self.description = description
        self.is_optional = is_optional_argument(field_type)
        self.has_default = has_default(default_value)
        self.is_variable = False
        if self.is_optional:
            self.is_scalar = field_type['kind'] == 'SCALAR'
        else:
            self.is_scalar = field_type['ofType']['kind'] == 'SCALAR'
        self.state = state
        self.types = types
        self.value = Value()
        if self.is_optional or self.has_default:
            self.symbol = 'â–¡'
        else:
            self.symbol = 'â—�'

    def is_string(self):
        pass

    def draw(self, stdscr, y, x, cursor, is_implementor=False):
        pass

    def key_left(self):
        pass

    def key_right(self):
        pass

    def key_left_right(self, key):
        pass

    def key(self, key):
        pass

    def select(self):
        pass

    def query(self, variables):
        pass

    def is_selected(self):
        pass

    def to_json(self, cursor):
        pass

    def from_json(self, data):
        pass

class EnumArgument(Node):

    def __init__(self, name, field_type, description, default_value, state, types):
        super().__init__()
        self.name = name
        self.type = get_type_string(field_type)
        self.description = description
        self.is_optional = is_optional_argument(field_type)
        self.has_default = has_default(default_value)
        self.is_variable = False
        if not self.is_optional:
            field_type = field_type['ofType']
        self.members = [value['name'] for value in find_type(types, field_type['name'])['enumValues']]
        self.state = state
        self.value = Value()
        if self.is_optional or self.has_default:
            self.symbol = 'â–¡'
        else:
            self.symbol = 'â—�'

    def draw(self, stdscr, y, x, cursor, is_implementor=False):
        pass

    def key_left(self):
        pass

    def key_right(self):
        pass

    def key_left_right(self, key):
        pass

    def key(self, key):
        pass

    def select(self):
        pass

    def query(self, variables):
        pass

    def is_selected(self):
        pass

    def to_json(self, cursor):
        pass

    def from_json(self, data):
        pass

class InputArgument(Node):

    def __init__(self, name, field_type, description, default_value, state, types):
        super().__init__()
        self.name = name
        self._type = get_type(field_type)['name']
        self.type = get_type_string(field_type)
        self.description = description
        self.is_optional = is_optional_argument(field_type)
        self.has_default = has_default(default_value)
        self.is_variable = False
        self.state = state
        self.types = types
        self.value = Value()
        if self.is_optional:
            fields = find_type(types, field_type['name'])['inputFields']
        else:
            fields = find_type(types, field_type['ofType']['name'])['inputFields']
        self.fields = ObjectFields(fields, [], types, state)
        self.fields.parent = self
        if self.is_optional or self.has_default:
            self.symbol = 'â–¡'
        else:
            self.symbol = 'â—�'
            self.child = self.fields[0]

    def draw_variable(self, stdscr, y, x, cursor):
        pass

    def draw_members(self, stdscr, y, x, cursor):
        pass

    def draw(self, stdscr, y, x, cursor, is_implementor=False):
        pass

    def key_left(self):
        pass

    def key_right(self):
        pass

    def key_left_right(self, key):
        pass

    def key(self, key):
        pass

    def key_variable(self):
        pass

    def select(self):
        pass

    def query(self, variables):
        pass

    def to_json(self, cursor):
        pass

    def from_json(self, data):
        pass

class ListItem(Node):

    def __init__(self, item, item_type):
        super().__init__()
        self.type = get_type_string(item_type)
        self.is_expanded = False
        self.item = item
        self.item.parent = self
        self.removed = False

    def draw_item(self, stdscr, y, x, i, number_of_items, cursor):
        pass

    def key(self, key):
        pass

    def key_left(self):
        pass

    def key_right(self):
        pass

    def select(self):
        pass

    def query(self, variables):
        pass

    def to_json(self, cursor):
        pass

    def from_json(self, data):
        pass

class ListArgument(Node):

    def __init__(self, name, field_type, description, default_value, state, types):
        super().__init__()
        self.name = name
        self.type = get_type_string(field_type)
        self.description = description
        self.is_optional = is_optional_argument(field_type)
        self.has_default = has_default(default_value)
        self.is_variable = False
        self.state = state
        self.field_type = field_type
        self.types = types
        self.value = Value()
        if self.is_optional or self.has_default:
            self.symbol = 'â–¡'
        else:
            self.symbol = 'â—�'
        self.items = []
        self.append_item()
        if self.symbol == 'â—�':
            self.child = self.items[0]

    def append_item(self):
        pass

    def draw_variable(self, stdscr, y, x, cursor):
        pass

    def draw_items(self, stdscr, y, x, cursor):
        pass

    def draw(self, stdscr, y, x, cursor, is_implementor=False):
        pass

    def item_selected(self, item):
        pass

    def item_removed(self, item):
        pass

    def select(self):
        pass

    def key(self, key):
        pass

    def key_variable(self):
        pass

    def query(self, variables):
        pass

    def to_json(self, cursor):
        pass

    def from_json(self, data):
        pass

class State:

    def __init__(self):
        self.cursor_at_input_field = False

def find_type(types, name):
    pass

def get_type(type_info):
    pass

def get_type_string(type_info):
    pass

def build_field(field, types, state):
    pass

def build_argument(argument, types, state):
    pass

class ObjectFieldsIterator:

    def __init__(self, fields):
        self._fields = fields
        self._index = 0

    def __next__(self):
        if self._index < len(self._fields):
            self._index += 1
            return self._fields[self._index - 1]
        else:
            raise StopIteration()

class ObjectFields:

    def __init__(self, arguments, fields, types, state):
        self._arguments_info = arguments
        self._fields_info = fields
        self._types = types
        self._state = state
        self._fields = None
        self.parent = None
        self._all_fields = None

    def set_next_and_prev(self):
        pass

    def fields(self):
        pass

    def __iter__(self):
        return ObjectFieldsIterator(self.fields())

    def __len__(self):
        return len(self.fields())

    def index(self, item):
        pass

    def get_argument(self, name):
        pass

    def get_field(self, name):
        pass

    def __getitem__(self, key):
        return self.fields()[key]

    def has_fields(self):
        pass

    def to_json(self, data, cursor):
        pass

    def from_json(self, data, cursor):
        pass

class MoveSelectedState:

    def __init__(self):
        self.new_cursor = None
        self.is_cursor_seen = False

class Tree:

    def __init__(self, schema, root, state):
        self._schema = schema
        self._root = root
        self._state = state
        self._cursor = root.fields[0]

    def cursor_type(self):
        pass

    def cursor_description(self):
        pass

    def draw(self, stdscr, y, x):
        pass

    def key_up(self):
        pass

    def key_down(self):
        pass

    def key_left(self):
        pass

    def key_right(self):
        pass

    def select(self):
        pass

    def key(self, key):
        pass

    def query(self):
        pass

    def go_to_begin(self):
        pass

    def go_to_end(self):
        pass

    def to_json(self):
        pass

    def from_json(self, data):
        pass

    def _move_cursor_to_selected_node_or_none(self):
        pass

    def _move_cursor_to_selected_node_or_none_level(self, node, state):
        pass

    def _find_first_below(self, node):
        pass

    def _find_last(self, node):
        pass

def load_tree_from_schema(schema):
    pass

def load_tree_from_json(data):
    pass
