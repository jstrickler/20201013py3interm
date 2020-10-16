#  Copyright (c) 2020. CJ Associates
import shutil

shutil.make_archive('DATA/cjapkg', 'zip', 'cja')


shutil.make_archive('DATA/cjapkg', 'gztar', 'cja')

shutil.make_archive('DATA/cjapkg', 'tar', 'cja')

shutil.make_archive('DATA/cjapkg', 'bztar', 'cja')

