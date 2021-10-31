import shutil
import os
import zipfile

#######  Basic file operations ########

#1. Moving files simply to another folder
practice_dir = r"/home/marci/Desktop/practice"
original_dir = r"/home/marci/Desktop/practice/sample.txt"
destination = r"/home/marci/Desktop/practice/practice_inside/sample.txt"

test_txt_from = r"/home/marci/Desktop/practice/practice_inside/sample3.txt"
test_txt_to = r"/home/marci/Desktop/practice/practice_inside/sample4.txt"

cont_txt_from = r"/home/marci/Desktop/practice/contentof.txt"
cont_txt_to = r"/home/marci/Desktop/practice/contentto.txt"

#Moving a file
def moveF():
    shutil.move(original_dir,destination)

#Renaming a file
def renameF():
    os.rename(test_txt_from,test_txt_to)

#Copying file
def copyF():
    shutil.copy(test_txt_from,practice_dir)

#Copy file contents
def copycontF():
    shutil.copyfile(cont_txt_from,cont_txt_to)

#Loop through files in a directory
def loopF():
    for file in os.listdir(practice_dir):
        print(practice_dir+'/'+file)

#Zipping files
def one_zipF():
    zip_name = 'test.zip'
    with zipfile.ZipFile(zip_name, 'w') as zipped:
        zipped.write(test_txt_from)

#Zipping all <some filetype> files in directory
def all_zipF(filetype: str):
    title = filetype.replace('.','')
    zip_name = f'all_{title}.zip'
    with zipfile.ZipFile(zip_name, 'a') as zipped:
        for file in os.listdir(practice_dir):
            if file.endswith('.txt'):
                zipped.write(file)


if __name__ == "__main__":
    #loopF()
    copyF()
    #copycontF()
    #one_zipF()
    #all_zipF('.txt')