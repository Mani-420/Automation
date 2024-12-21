# Main file. Creation, open and writing fileswill be done from here.


# Opening and Reading a file 
with open('File_handling/New_Method/open.txt', "r") as file1:
    text1 = file1.read()
    print(text1)


# Writing a file 
with open('File_handling/New_Method/write.txt', "w") as file2:
    content = input("Enter something to write in a file: ")
    text2 = file2.write(content)


# Appending a file 
with open('File_handling/New_Method/append.txt', "a") as file2:
    content = input("Enter something to add in a file: ")
    text2 = file2.write(f"\n{content}")