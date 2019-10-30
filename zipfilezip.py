import os
from zipfile import ZipFile


## Get the base name for the project and store it
base_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
file_path = os.path.dirname(os.path.abspath(__file__))          #Current files filepath



directory = r"C:\Users\Ian\Documents\PersonalProjects\Backups"


def get_all_file_paths(directory): 
  
    # initializing empty file paths list 
    file_paths = [] 
  
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 
  
    # returning all file paths 
    return file_paths  

def main(): 
    # path to folder which needs to be zipped 
    zip_directory = '.'
    #base_dir = '{}{}'.format(directory, "\ ".strip())
    target_dir = directory

    # Initialize base vars
    dirList = list()
    dirLength = 0

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
    f_name = "{}_{}_{}{}".format("BKUP", base_name, f_num, ".zip")          #File Name

    # calling function to get all file paths in the directory 
    file_paths = get_all_file_paths(zip_directory) 
  
    # printing the list of all files to be zipped 
    print('Following files will be zipped:') 
    for file_name in file_paths: 
        print(file_name) 
  
    # writing files to a zipfile 
    with ZipFile(f_name,'w') as zip: 
        # writing each file one by one 
        for file in file_paths: 
            zip.write(file, f_name) 
  
    print('All files zipped successfully!')         
  
  
if __name__ == "__main__": 
    main()