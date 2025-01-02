# Getting the Current working directory
import os 
cwd = os.getcwd() 
print("Current working directory:", cwd) 

# --------------------------------------------------------

# Changing the Current working directory
import os 
def current_path(): 
    print("Current working directory before") 
    print(os.getcwd()) 
    print() 
current_path() 
os.chdir('../') 
current_path() 
