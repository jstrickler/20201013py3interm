#  Copyright (c) 2020. CJ Associates
from glob import glob

db_files = glob('DATA/*.db')
print(db_files, '\n')

text_files = glob('DATA/*.txt')
print(text_files, '\n')

bazinga_files = glob('DATA/*.bazinga')
print(bazinga_files)

