"""
Description:
    Collection of functions for use with dictionary operations
"""

# import system modules
import json
import collections
import string
from base64 import b64encode, b64decode


def encode(data):
    """
    Description:
        encodes string elements of a dictionary to base64

    Parameters:
        data - dictionary

    Returns:
        dictionary
    """
    if isinstance(data, basestring):
        return b64encode(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(encode, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(encode, data))
    else:
        return data


def decode(data):
    """
    Description:
        decodes base64 elements of a dictionary to string

    Parameters:
        data - dictionary

    Returns:
        dictionary
    """
    if isinstance(data, basestring):
        return b64decode(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(decode, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(decode, data))
    else:
        return data


def clean_dict(data):
    """
    Description:
         removes non-printable characters from dictionary elements

    Parameters:
        data - python dictionary

    Returns:
        python dictionary with non-printable characters removed
    """
    if isinstance(data, basestring):
        return filter(lambda x: x in string.printable, data)
    elif isinstance(data, collections.Mapping):
        return dict(map(clean_dict, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(clean_dict, data))
    else:
        return data


def convert_tuple_to_dict(t):
    """ Convert a tuple of tuples to dictionary """
    d = {}
    for i in t:
        d.setdefault(i[0], []).append(i[1])
    return d


def convert_dict_to_json(data, fix=""):
    """
    Description:
        converts a dictionary to a json object

    Parameters:
        data - python dictionary

        fix  - performs operation on dictionary before converting
               clean  - removes non-printable characters
               encode - encodes strings to base64

    Returns:
        json object
    """
    if fix.lower() == "clean":
        data = clean_dict(data)
    elif fix.lower() == "encode":
        data = encode(data)
    return json.dumps(data)


def convert_json_to_dict(data, fix=""):
    """
    Description:
        converts a json object to a dictionary

    Parameters:
        data - json object

        fix  - performs operation on dictionary before converting
               encode - encodes strings to base64

    Returns:
        json object
    """
    if fix.lower():
        data = decode(data)
    return json.loads(data)


def combine_dicts(dict_list):
    """ combine a list of dictionaries into one dictionary """
    super_dict = {}
    for d in dict_list:
        for k, v in d.iteritems():
            super_dict.setdefault(k, v)
    return super_dict


def convert_ordered_to_dict(input_ordered_dict):
    """ convert an ordered dictionary to standard dictionary """
    return json.loads(json.dumps(input_ordered_dict))
