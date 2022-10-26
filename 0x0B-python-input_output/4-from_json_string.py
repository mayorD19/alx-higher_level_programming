#!/usr/bin/python3
"""A function that returns the str
from a JSON representation
"""

import json


def from_json_string(my_str):
    """A return of the string(A python object) 
    from a JSON representation
    """
    return json.loads(my_str)
