import os

dir_path = r"C:\Users\1100a\Pictures"

files = os.listdir(dir_path)

for file in files:
    file_path = os.path.join(dir_path, file)
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file_path)[1]
        dest_folder = os.path.join(dir_path, file_ext[0:])
        os.makedirs(dest_folder, exist_ok=True)
        os.replace(file_path, os.path.join(dest_folder, file)) 