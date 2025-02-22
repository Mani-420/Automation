import shutil

# For single file:--------------------------------------
shutil.copy("C:\\Users\\DELL\\Desktop\\extra.txt", "C:\\Users\\DELL\\Desktop\\New folder")


# For multiple files:-----------------------------------
shutil.copytree("C:\\Users\\DELL\\Desktop\\New folder", "C:\\Users\\DELL\\Desktop\\Newfolder_backup")


# For Moving files:-------------------------------------
shutil.move("C:\\Users\\DELL\\Desktop\\extra.txt", "C:\\Users\\DELL\\Desktop\\New folder")
