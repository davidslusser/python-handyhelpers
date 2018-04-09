import os
import sys

parent_path = os.path.abspath("{}/..".format(os.path.dirname(os.path.abspath(__file__))))
if parent_path not in sys.path:
    sys.path.insert(0, parent_path)
