# If the path exist then os.mkdir() is used.
import os

# Define the directory name and parent path
directory = "Listing"
parent_dir = "F:\Goals\Automation\OS_Module"

# Join the paths to form the complete path
path = os.path.join(parent_dir, directory)

# Create the directory
os.mkdir(path)
print("Directory '%s' created" % directory)

# -----------------------------------------------------
# If the path does not exist then os.makedirs() is used.