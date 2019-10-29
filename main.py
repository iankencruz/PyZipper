"""" Python Application to zip up files and rename it recursively  """

from os.path import basename
import os, shutil, zipfile


## Get the base name for the project and store it
base_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
file_path = os.path.dirname(os.path.abspath(__file__))          #Current files filepath

# path to folder which needs to be zipped 
directory = os.getcwd()
base_dir = '{}{}'.format(directory, "\ ".strip())
target_dir = base_dir + "\Backup"

# Initialize base vars
dirList = list()
dirLength = 0





def main():

    print("CWD: " + os.getcwd())
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
        print("Folder dooes not exist")
    else:
        print("Folder exists")
        dirList = os.listdir(target_dir)
        dirLength = len(dirList)
        print(dirList)
        print(dirLength)
    
    f_num = str(dirLength).zfill(2)
    f_name = "{}_{}_{}".format("BKUP", base_name, f_num)

    shutil.make_archive(f_name, "zip", os.getcwd())
    
    archived = "{}\{}{}".format(os.getcwd(), f_name, ".zip")
    print("ArchivedFile: " +  archived)
    print("Make_Archive Complete!")


    

# run Main function
if __name__ == "__main__": 
    main() 
