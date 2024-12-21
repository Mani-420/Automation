# Main file. Creation, open and writing fileswill be done from here.


# Opening and Reading a file 
# file1 = open('open.txt', "r")
# text1 = file1.read()
# print(text1)
# file1.close()


# Writing a file 
# file2 = open('write.txt', "w")
# text2 = input("Enter something to write in a file: ")
# file2.write(text2)
# file2.close()


# Writing a file 
file3 = open('append.txt', "a")
text3 = input("Enter something to add in a file: ")
file3.write(f"\n{text3}")
file3.close()