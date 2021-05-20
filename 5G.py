import os
from fileserver.settings import BASE_DIR
print(BASE_DIR)
def getFlist(BASE_DIR):
    for root, dirs, files in os.walk(BASE_DIR):
        print('root_dir:', root)
        print('sub_dirs:', dirs)
        print('files:', files)
        return files

flist = getFlist(BASE_DIR)
print(flist)