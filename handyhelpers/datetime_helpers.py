"""
Description:
    Collection of functions for use with datetime operations
"""

import datetime


def is_leap_year(dt):
    """
    Description:
        Determines if the year in a provided datetime object is a leap year.
    Parameters:
        dt = datetime object
    Returns:
        True if year is a leap year
        False if year is not a leap year
    """
    year = dt.year
    if not year % 4 and not year % 100 and not year % 400:
        return True
    if not year % 4 and year % 100:
        return True
    return False


def get_days_in_year(dt):
    """
    Description:
        Determines number of days in year for a provided datetime object.
    Parameters:
        dt = datetime object
    Returns:
        number of days in year (integer value)
    """
    if is_leap_year(dt):
        return 366
    return 365


def get_days_in_month(dt):
    """
    Description:
        Determines number of days in month for a provided datetime object.
    Parameters:
        dt = datetime object
    Returns:
        number of days in month (integer value)
    """
    if is_leap_year(dt):
        days_in_month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    else:
        days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return days_in_month[dt.month]


def get_week_of_month(dt):
    """
    Description:
        Returns the week number of the month for a provided datetime object.
    Parameters:
        dt = datetime object
    Returns:
        week number of month (integer value)
    """
    weekday = dt.strftime('%A')
    dom = dt.day
    count = 0
    for i in range(dom):
        if dt.strftime('%A') == weekday:
            count += 1
        dt += datetime.timedelta(days=1)
    return count
