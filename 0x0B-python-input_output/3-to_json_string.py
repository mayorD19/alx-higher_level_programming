#!/usr/bin/python3
"""A function that imports from the json library and
returns the JSON representation of an object(string)
"""

import json


def to_json_string(my_obj):
    """The Module that returns the JSON representation of the object
    """
    return json.dumps(my_obj)
