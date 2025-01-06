import os 
file = 'extra.py'
location = "F:\Goals\Automation\OS_Module\Listing"
path = os.path.join(location, file) 
os.remove(path) 

directory = "Listing"
parent = "F:\Goals\Automation\OS_Module"
path = os.path.join(parent, directory) 
os.rmdir(path) 