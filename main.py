"""" Python Application to zip up files and rename it recursively  """

from os.path import basename
from zipfile import ZipFile
import os, shutil



## Get the base name for the project and store it
base_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))


def zipdir(path, zip_File):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            zip_File.write(os.path.join(root, file))
            print(files)

def create_zip(dir, file_name):
    zipf = ZipFile(dir + "\ " +  file_name, "w")
    zipdir(dir, zipf)
    zipf.close()

def main():
    

    # path to folder which needs to be zipped 
    directory = os.getcwd()
    dst = directory + base_name + "\Backup\ ".strip()

    targetDir = '{}\{}\{}'.format(directory, base_name,"Backup")
    dirLength = 0

    # Check if backup folder already exist
    # if not -> create a backup folder
    if not os.path.exists(targetDir):
        os.mkdir(targetDir)

    else:   
        # print ("Path exists")
        dirList = os.listdir(targetDir)
        dirLength = len(dirList)   

    # writing files to a zipfile     
    # file name and number
    f_num = str(dirLength).zfill(2)
    f_name = '{}_{}{}'.format(base_name, f_num, ".zip")

    print("TARGETDIR: " + dst)        ###DEBUG

    

   
        

        
    
    try:
        create_zip(targetDir, f_name)
        print("ZipFile created Successfully!")
    except FileExistsError:
        print("Cannot Find File")
        return
  

    

# run Main function
if __name__ == "__main__": 
    main() 
