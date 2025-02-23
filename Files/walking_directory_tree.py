import os

for folderName, subFolders, fileNames in os.walk("C:\\Users\\DELL\\Desktop\\New folder"):
    print("The folder is, " + folderName)
    print("The sub folder in, "+ folderName + " are " + str(subFolders))
    print("The filename in, "+ folderName + " are " + str(fileNames))
    print()
    
