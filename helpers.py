#!/usr/bin/env python3

import os

def get_path():
    """ Asks to the user for the path of the directory and returns
    the path if it is valid"""

    path = input("Directory path: ")
    if os.path.isdir(path):
        return path
    else:
        raise(ValueError)

if __name__ == "__main__":
    get_path()
    

