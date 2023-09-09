import os
import sys
import pathlib
import zipfile

dirname = input("Enter Directory name that you want to backup: ")

if not os.path.isdir(dirname):
    print("Directory", dirname, "doesn't exist")
    sys.exit(0)
curDirectory = pathlib.Path(dirname)

with zipfile.ZipFile("myZip.zip", mode = "w") as archieve:
    for file_path in curDirectory.rglob("*"):
        archieve.write(file_path, arcname = file_path.relative_to(curDirectory))

if os.path.isfile("myZip.zip"):
    print("Archieve", "myZip.zip", "Created Successfully")
else:
    print("Error in creating zip archieve")