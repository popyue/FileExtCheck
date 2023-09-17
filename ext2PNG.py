import os
import sys
import pathlib

#basePath = '/Users/leowu/Documents/HTB/Image/IMG/'

def addExt(base):
    entries = sorted(os.listdir(base))
    for entry in entries:
        #print(entry) # Debug
        targetDirs = base+entry # Set up target directory 
        targetFiles = os.listdir(targetDirs) # Get all the target file in directory
        index = 0 # initial the index value
        while index < len(targetFiles):
            targetFileName = targetFiles[index] # Initialize parameter, setup target file name
            targetPath = pathlib.Path(targetDirs+'/'+targetFileName) # Instance the target file in specify path
            FileSuffix = targetPath.suffix # Get File origin suffix(extension)
            # Check extension exist or not
            if FileSuffix == '':
                newFilePath = targetPath.with_suffix(".png") # add new extension
                print("old file name: {}".format(targetPath)) # Debug
                print("new file name: {}".format(newFilePath)) # Debug
                targetPath.rename(newFilePath) # Rename file to origin one
            index += 1 # index increase
        

## Change the directory name
## Name Format: [IMG]<name>
## Done 
def renameDir(base):
    targetDir = sorted(os.listdir(base)) # Sort dir in target path
    index = 0 # initial the index value
    while index < len(targetDir):
        targetPath = pathlib.Path(base+targetDir[index]) # Instance the dir in specify path
        print(targetDir[index]) # Print all dir(Debug)
        targetPath.rename(base+"[IMG]"+str(targetDir[index])) # Change Name
        index += 1 # index increase

def main():
    basePath = '/Users/<myusername>/Documents/HTB/Image/IMG/'
    #renameDir(basePath)
    #addExt(basePath)

if __name__ == '__main__':
    main()

