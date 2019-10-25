"""" Python Application to zip up files and rename it recursively  """

from os.path import basename
from zipfile import ZipFile
import os, shutil


cwd = os.getcwd()

## Get the base name for the project and store it
base_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))

def get_all_file_paths(directory):
    file_paths = [] 


    #crawl through folder directory
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join two strings together to form full filepath
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths



def main():
    

    # path to folder which needs to be zipped 
    directory = cwd
    dst = cwd + base_name + "\Backup\ ".strip()
    targetDir = '{}\{}\{}'.format(cwd, base_name,"Backup")
    file_paths = get_all_file_paths(directory)
    
    print("DST: " + targetDir)

    # Check if backup folder already exist
    #if not -> create a backup folder
    if not os.path.exists(targetDir):
        os.mkdir(targetDir)
    else:   
        print ("Path exists")
        dirList = os.listdir(targetDir)
        dirListAmount = len(dirList)        

        # printing the list of all files to be zipped 
        print('Following files will be zipped:') 
        for file_name in file_paths: 
            print(file_name) 
            
        # writing files to a zipfile     
        # file name and number
        f_num = str(dirListAmount).zfill(2)
        f_name = '{}_{}{}'.format(base_name, f_num, ".zip")

        print(f_name)
    
        try:
            with ZipFile(dst + f_name,'w') as zip: 
            # writing each file one by one 
                for file in file_paths: 
                    zip.write(file) 

            print('All files zipped successfully!')  
        except:
            print("Cannot zip files!")
  
    


if __name__ == "__main__": 
    main() 
