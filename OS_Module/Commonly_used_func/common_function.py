import os
print(os.name)


# ---------------------------------------------------------
# Rename file 
fd = "F:\Goals\Automation\OS_Module\Commonly_used_func\cmmon_func.py"
os.rename(fd,'common_function.py')


# ---------------------------------------------------------
# Remove file 
os.remove("F:\Goals\Automation\OS_Module\Commonly_used_func\extra.py")
