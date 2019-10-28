#!/usr/bin/env python
import os
import zipfile
import shutil




## Get the base name for the project and store it
base_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))

# path to folder which needs to be zipped 
directory = os.getcwd()
dst = directory + base_name + "\Backup\ ".strip()

targetDir = '{}\{}'.format(directory, "Backup")


if not os.path.exists(dst):
    os.mkdir(targetDir)
    print("Dir Did not exist, Creating one now!")

zipp = shutil.make_archive("ZippyTest", "zip", targetDir, os.getcwd() )
print("Dir Exists")
shutil.move(targetDir + "\ZippyTest.zip", dst)

