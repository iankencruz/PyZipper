import os
import zipfile

zf = zipfile.ZipFile("myzipfile.zip", "w")
for dirname, subdirs, files in os.walk(os.getcwd()):
    #zf.write(dirname)
    #print(dirname)
    for filename in files:
        print(filename)
        zf.write(os.path.join(dirname, filename))
        
zf.close()
print("Finished Zipping Files!")