#  Copyright (c) 2020. CJ Associates

class FileInfo:

    def __init__(self, file_path):
        self._file_path = file_path

        # get the low-level info here....

    @property
    def size(self):
        pass

    @property
    def modtime(self):
        pass

if __name__ == '__main__':

    f = FileInfo("spam.txt")
    print(f.size, f.modtime, f.permissions)

