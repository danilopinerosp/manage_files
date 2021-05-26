#!/usr/bin/env python3

import os
import subprocess
from datetime import datetime

def get_path():
    """ Asks to the user for the path of the directory and returns
    the path if it is valid"""

    path = input("Directory path: ")
    if os.path.isdir(path):
        return path
    else:
        raise(ValueError)

def create_directory(path, name):
    """ Create a directory in path if the directory does not exist yet"""
    new_path = os.path.join(path, name)
    if not os.path.isdir(new_path):
        subprocess.run(['mkdir', new_path])

def create_directories(path):
    """ Create the directories to classify the files"""
    directories = ['images', 'pdf', 'videos', 'audio', 'spreedsheet', 'text', 'scripts', 'docs', 'other']
    for directory in directories:
        create_directory(path, directory)

def rename_file(path, old_name, new_name):
    """ The funcion renames a file that is in the path given as argument. Old_name is the current
    name of the file and new_name is the name to change into"""
    
    old_file = os.path.join(path, old_name)
    new_file = os.path.join(path, new_name)
    os.rename(old_file, new_file)

def standardized_name(path, filename):
    """ Takes a path and a filename in it and return a string with the new name according to
    the time of most recent content modification"""
    path_file = os.path.join(path, filename)
    stat = os.stat(path_file)
    extension = path_file.split('.')[-1]
    creation_time = datetime.fromtimestamp(stat.st_mtime).strftime('%m-%d-%Y_%H:%M:%S')
    return '{}.{}'.format(creation_time, extension)

def classify_file(filename, categories):
    """ Classify filename according to its extension.
    Arguments:
    ---------
    categories: dict. The categories as the keys and the extensions the values for each key
    """
    extension = filename.split('.')[-1]
    for category, extensions in categories.items():
        if extension in extensions:
            return category
    return 'other'


if __name__ == "__main__":
    categories = {'images': ['png', 'jpeg'], 'text':['txt']}
    for directory in categories.keys():
        print(directory)
    

    

