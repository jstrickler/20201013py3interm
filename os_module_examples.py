import os   # also imports os.path
import pathlib

print(dir(os))
print('-' * 60)

FOLDER = "DATA"
FILE_NAME = "mary.txt"

file_path = os.path.join(FOLDER, FILE_NAME)
print("file path:", file_path)

print(os.path.basename(file_path))
print(os.path.dirname(file_path))
print(os.path.abspath(file_path))

file_size = os.path.getsize(file_path)
print("file size:", file_size)

for f in 'DATA/mary.txt', 'mary.txt', file_path, "wombats!", 'ANSWERS/copy_files.py', 'DATA':
    print(f, os.path.exists(f), os.path.isfile(f), os.path.isdir(f))
print()

file_list = os.listdir("DATA")
print(file_list)

print(os.listdir('.'))

for entry in pathlib.Path('.').iterdir():
    if entry.is_file():
        print(entry.name)

f = pathlib.Path("DATA/wombats.txt")
print(f.exists())
