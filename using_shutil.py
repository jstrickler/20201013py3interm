#  Copyright (c) 2020. CJ Associates
import shutil
import os

# better than os.system("copy spam.py ham.py")
shutil.copy('spam.py', 'ham.py')

if os.path.exists('classes_CARDS.pdf'):
    shutil.move('classes_CARDS.pdf', 'classes_carddeck.pdf')

# shutil.rmtree("foo/bar")  # rm -rf

os.unlink('ham.py')  # rm

print(shutil.disk_usage('.'))   # du


