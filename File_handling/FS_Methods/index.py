with open ("File_handling/FS_Methods/myFile.txt", "r") as file1:
    while True:
        line = file1.readline()
        if not line:
            break
        print (line)
