#  Copyright (c) 2020. CJ Associates
import os  # includes os.path
from datetime import datetime

file_path = "DATA/mary.txt"

raw_file_mod_time = os.path.getmtime(file_path)
print(raw_file_mod_time)

file_mod_time = datetime.fromtimestamp(raw_file_mod_time)

print(file_mod_time)

file_info = os.stat(file_path)
print(file_info)
print(str(oct(file_info.st_mode))[-3:])

# chmod 755 myfile
# os.access(file, PERM)   #  perm is any of os.R_OK os.W_OK os.X_OK

file_size = os.path.getsize(file_path)
print(file_size)

print(dir(os.path))
print('-' * 60)
print(dir(os))

