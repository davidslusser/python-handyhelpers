"""
Description:
    Collection of functions for use with dictionary operations
"""

import collections
import itertools
import operator


# import system modules
import os
import sys
import yaml
import re
import json
import collections
import itertools
import logging
import string


# import custom modules
from scriptUtils import *




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


def convertDictToObj(d):
    """ Converts a dictionary to a python class object """
    return Struct(**d)


def convertYamlToDict(file_name):
    """
    Description:
        Get contents of a yaml file and return as dictionary

    Parameters:
        file_name   - name of yaml file

    Returns:
        dictionary
    """
    config = {}
    if os.access(file_name, os.F_OK):
        with open(file_name, 'r') as f:
            config = yaml.load(f)
    else:
        logging.info("can not find %s", file_name)
    return config


def convertDictToYaml(data, file_name):
    """ Writes the contents of a dictionary data to a yaml file """
    with open(file_name, "w") as outfile:
        outfile.write(yaml.dump(data, default_flow_style=False))


def convertTupleToDict(t):
    """ Convert a tuple of tuples to dictionary """
    d={}
    #[ valDict.setdefault(i[0],i[1]) for i in values ]
    for i in t:
        d.setdefault(i[0],[]).append(i[1])
    return d


def cleanDict(data):
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
        return dict(map(cleanDict, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(cleanDict, data))
    else:
        return data


def convertDictToJson(data, fix=""):
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
        data = cleanDict(data)
    elif fix.lower() == "encode":
        data = encode(data)
    return json.dumps(data)


def convertJsonToDict(data, fix=""):
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


def convertListToJson(data, key, fix=""):
    """
    Description:
        converts a list to a json object

    Parameters:
        data - python list

        key  - key or name of list

        fix  - performs operation on dictionary before converting
               clean  - removes non-printable characters
               encode - encodes strings to base64
    """
    data = {key:data}
    if fix.lower() == "clean":
        data = cleanDict(data)
    elif fix.lower() == "encode":
        data = encode(data)
    return json.dumps(data)


def combineDicts(dict_list):
    """ combine a list of dictionaries into one dictionary """
    super_dict = {}
    for d in dict_list:
        for k, v in d.iteritems():
            super_dict.setdefault(k, v)#.append(v)
    return super_dict


def convertOrderedToDict(input_ordered_dict):
    """ convert an ordered dictionary to standard dictionary """
    return json.loads(json.dumps(input_ordered_dict))


def listRecursive(d, key, path=None):
    """ get the value(s) for a given key in a dictionary """
    if not path: path = []
    for k, v in d.items ():
        if isinstance(v, collections.OrderedDict):
            for path, found in listRecursive(v, key, path + [k] ):
                yield path, found
        if k == key:
            yield path + [k], v


def getValues(d, key):
    """ get values of key from dictionary """
    for path, found in listRecursive(d, key):
        data = (path, found)
    return convertOrderedToDict(data[1])

