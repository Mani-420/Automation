import os
print(os.name)


# ---------------------------------------------------------
# Rename file 
fd = "F:\Goals\Automation\OS_Module\Commonly_used_func\cmmon_func.py"
os.rename(fd,'common_function.py')


# ---------------------------------------------------------
# Remove file 
os.remove("F:\Goals\Automation\OS_Module\Commonly_used_func\extra.py")


# ---------------------------------------------------------
# Checking the existing file (a file exist or not)
result = os.path.exists("Curr_dir.py")
print(result) 


# ---------------------------------------------------------
# To get the size of the file
size = os.path.getsize("Curr_dir.py")
print("Size of the file is", size," bytes.")