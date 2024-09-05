import os
from pathlib import Path

user_directory = Path("~").expanduser()
folder_path = user_directory / input("enter the path: ~/")
file_name = input("enter the default name for the files: ")

for count, filename in enumerate(os.listdir(folder_path)):
    count += 1

    if not filename.startswith(file_name):
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, file_name + str(count) + ".jpg")

        while os.path.exists(dst):
            count += 1
            dst = os.path.join(folder_path, file_name + str(count) + ".jpg")

        os.rename(src, dst)

input('success! press enter')