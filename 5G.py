# -- coding:utf-8 --
# import os
# from fiercer.settings import BASE_DIR
# print(BASE_DIR)
# def getFlist(BASE_DIR):
#     for root, dirs, files in os.walk(BASE_DIR):
#         print('root_dir:', root)
#         print('sub_dirs:', dirs)
#         print('files:', files)
#         return files
#
# flist = getFlist(BASE_DIR)
# print(flist).
import os


def saveToFile(saveFile, content):
    try:

        tf = open(saveFile, 'w+b')
        tf.write(content)
        tf.close()
        os.rename(saveFile, saveFile)
        return True
    except Exception as e:
        print(e)
        return False


import sys

tf = open('GETAIRPRESSUREDATALIST.dmp', 'r+b')
ccd = tf.readline().decode('ascii')
print(ccd)
tf.close()
