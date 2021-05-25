#!/usr/bin/env python3

import os
import subprocess

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
        subprocess.run(['mkdir', name])

def create_directories(path):
    """ Create the directories to classify the files"""
    directories = ['images', 'pdf', 'videos', 'audio', 'spreedsheet', 'text', 'scripts', 'docs', 'other']
    for directory in directories:
        create_directory(path, directory)

    

if __name__ == "__main__":
    create_directories(get_path())
    

