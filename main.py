"""" Python Application to zip up files and rename it recursively  """

from os.path import basename
from zipfile import ZipFile
import os, shutil


dst = r"C:\Users\iankr\Documents\Kens Folder\Projects\PyZipper\Zips\ "
cwd = os.getcwd()

## Get the base name for the project and store it
projectName = basename(cwd)
print ("BaseName = " + projectName)

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

    file_paths = get_all_file_paths(directory)

    # printing the list of all files to be zipped 
    print('Following files will be zipped:') 
    for file_name in file_paths: 
        print(file_name) 


    zipfileName = projectName + ".zip"

    


    # writing files to a zipfile 
    with ZipFile(dst + zipfileName,'w') as zip: 
        # writing each file one by one 
        for file in file_paths: 
            zip.write(file) 
  
    print('All files zipped successfully!')  



if __name__ == "__main__": 
    main() 




# Iterate through all files inside of project and add to zip file




# check if file already exist ( if exist add iteration number to the end) 

#print ("CWD = " + cwd)
#print ("DST = " + dst)
