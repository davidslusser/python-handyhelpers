"""
Description:
    Collection of functions for use in Linux (or Linux-like) shells
"""

import os
import logging
import datetime
import subprocess


def remove_by_age(path, file_type="html", age=7):
    """
    Description:
        remove files of a certain age from a specified location

    Parameters:
        path      - path of directory to evaluate
        file_type - type (by extension) of files to remove
        age       - file age in days

    Returns:
        0 - if successful
        1 - if exception encountered
    """
    try:
        delete_age = datetime.datetime.now() - datetime.timedelta(days=age)
        if file_type:
            if not file_type.startswith("."):
                file_type = "." + file_type
            file_list = ["{}/{}".format(path, i) for i in os.listdir(path)
                         if os.path.isfile("{}/{}".format(path, i)) and i.endswith(file_type)]
        else:
            file_list = ["{}/{}".format(path, i) for i in os.listdir(path) if os.path.isfile("{}/{}".format(path, i))]

        logging.info('removing {} files from {} that are older than {} days'.format(file_type, path, age))
        for f in file_list:
            ts = datetime.datetime.fromtimestamp(os.stat(f).st_mtime)
            if ts < delete_age:
                logging.info(f)
                os.remove(f)
        return 0
    except Exception as err:
        logging.error(err)
        return 1


def run_shell_command(cmd):
    """
    Description:
        execute a shell command and capture output, error, and exit code

    Parameters:
        cmd - command to be executed

    Returns:
        return code (rc), output (out), and error (err) or (1,1,1) if exception encountered
    """
    try:
        proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        rc = proc.returncode
        return rc, out, err
    except Exception as err:
        logging.error(err)
        return 1, 1, 1
