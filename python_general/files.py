import os
import shutil

#######  Basic file operations ########

#1. Moving files simply to another folder
original_dir = r"/home/marci/Desktop/practice/sample.txt"
destination = r"/home/marci/Desktop/practice/practice_inside/sample.txt"
test_txt = r"/home/marci/Desktop/practice/practice_inside/sample.txt"


shutil.move(original_dir,destination)