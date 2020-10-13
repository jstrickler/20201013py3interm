import os

START_DIR = "."

for curr_dir, dir_list, file_list in os.walk(START_DIR):
    print(curr_dir)
    for file_name in file_list:
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_dir, file_name)
            file_size = os.path.getsize(file_path)
            file_mod_time = os.path.getmtime(file_path)
            print(f"    {file_size:6d} {file_name} {file_mod_time}")



