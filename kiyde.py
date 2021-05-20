import os

from fileserver.settings import BASE_DIR
print(BASE_DIR)
def file_name(file_path):
    sisete = {}
    for x in os.walk(file_path):
        # print(root)
        #
        # print(dirs)
        #
        # print(files)
        # print(x)
        print(x)
        # sisete[x[0]]=x[1]
    return sisete

print(file_name(BASE_DIR))

