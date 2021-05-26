#!/usr/bin/env python3

import os
from helpers import get_path, create_directory, standardized_name, rename_file, classify_file
import subprocess

def main():
    
    categories = {'images': ['png', 'jpeg', 'jpg', 'img'], 'pdf': ['pdf'],
                  'videos': ['mp4'], 'audio': ['mp3'], 'spreedsheet': ['xlsx'],
                  'text': ['txt'], 'scripts': ['py', 'c', 'cpp', 'js'], 'docs': ['docs']}

    path = get_path()


    # Get the files that are in the directory
    files = os.listdir(path)

    for f in files:
        if os.path.isfile(os.path.join(path,f)):
            st_name = standardized_name(path, f)
            new_name = rename_file(path, f, st_name)
            cat = classify_file(f, categories)
            if not os.path.isdir(os.path.join(path, cat)):
                create_directory(path, cat)
            old_path = os.path.join(path, st_name)
            new_path = os.path.join(path, cat, st_name)
            subprocess.run(['mv', old_path, new_path])

if __name__ == "__main__":
    main()

