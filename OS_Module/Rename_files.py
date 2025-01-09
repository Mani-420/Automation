import os

# Specify the folder path
folder_path = r"F:\Goals\Special"

try:
    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Sort the files to ensure consistent renaming order
    files.sort()
    
    # Rename the files
    for index, file_name in enumerate(files, start=1):
        old_path = os.path.join(folder_path, file_name)
        new_name = f"file{index}{os.path.splitext(file_name)[1]}"  # Preserve original file extension
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {file_name} -> {new_name}")
    
    print("All files renamed successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
