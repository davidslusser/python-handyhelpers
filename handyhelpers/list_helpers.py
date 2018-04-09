"""
Description:
    Collection of functions for use with list operations
"""

import itertools
import operator


def slice_list(l, size, remainder=True):
    """
    Description:
        slice an existing list into multiple smaller lists

    Parameters:
        l         - list containing items (to be sliced)
        size      - number of elements to include in sliced lists
        remainder - include sublist of remainder items (smaller then 'size')

    Returns:
        list of lists
    """
    if remainder:
        return [l[x:x+size] for x in xrange(0, len(l), size)]
    else:
        return [l[x:x+size] for x in xrange(0, len(l), size) if len(l[x:x+size]) == size]


def group_consecutive(l, size):
    """
    Description:
        Group elements of a given list into sublists when elements are consecutive

    Parameters:
        l    - list (of numberic values) to be evaluated
        size - size of sublists

    Returns:
        list of lists
    """
    l.sort()
    my_list = []
    for k, g in itertools.groupby(enumerate(l), lambda (i, x): i-x):
        tmp = map(operator.itemgetter(1), g)

        # get equal size group
        if len(tmp) == size:
            my_list.append(tmp)

        # Evaluate larger group
        elif len(tmp) > size:
            tmp_list = [tmp[x:x+size] for x in xrange(0, len(tmp), size) if len(tmp[x:x+size]) == size]
            my_list.extend(tmp_list)
    return my_list


def flatten_lists(*l):
    """
    Description:
        combines multiple lists into one

    Parameters:
        l      - list(s) to flatten

    Returns:
        single list containing all elements
    """
    return list(itertools.chain.from_iterable(l))


def flatten_lists_unique(*l):
    """
    Description:
        combines unique elements of multiple lists into one list

    Parameters:
        l - list(s) to flatten

    Returns:
        single list containing unique elements
    """
    return list(set(itertools.chain.from_iterable(l)))


def flatten_lists_common(*l):
    """
    Description:
        combines common elements of multiple lists into one list

    Parameters:
        l - list(s) to process

    Returns:
        single list of common elements
    """
    master_list = [i for i in l if i]
    if master_list:
        return list(set(master_list[0]).intersection(*master_list))
    return []


def reverse_nested(l):
    """
    Description:
        Reverse a list of lists; outer list and nested lists will both be reversed

    Parameters:
        l - nested list to reverse

    Returns:
        reversed nested list
    """
    result = []
    for i in l:
        if isinstance(i, list):
            result.append(reverse_nested(i))
        else:
            result.append(i)
    result.reverse()
    return result


def get_longest_length(l):
    """ Return length of the longest list in a list of lists """
    if not l:
        return None
    return max([len(i) for i in l])


def get_shortest_length(l):
    """ Return length of the longest list in a list of lists """
    if not l:
        return None
    return min([len(i) for i in l])


def get_x_elements(l, x=0):
    """
    Description:
        Get only the 'x' element of each list in a list of lists

    Parameters:
        l = lists of lists
        x = sub-list index

    Returns:
        single list containing only the x element of each sub-list
    """
    if x > get_longest_length(l):
        return []
    return_list = []
    for i in l:
        try:
            return_list.append(i[x])
        except IndexError:
            break
    return return_list


def is_list_type(l, list_type=int):
    """
    Description:
        Test if all elements in a list are a specific type

    Parameters:
        l         - list to test
        list_type - type to test

    Returns:
        True if all elements are desired type
        False if any element is not desired type
    """
    return all(isinstance(x, list_type) for x in l)


def is_consecutive(l, step=1):
    """
    Description:
        Test if all elements in a list are consecutive integers

    Parameters:
        l    - list of integers
        step - space between digits

    Returns:
        True if list is consecutive
        False if list is not consecutive
    """
    if sorted(l) == range(min(l), max(l) + 1, step):
        return True
    return False
