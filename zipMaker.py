import os
from os import listdir
from os.path import isfile, join
from time import sleep
from shutil import make_archive
from zipfile import ZipFile
rawPath = "/home/rezapish/Desktop/comp and raw/raw"
compressedPath = "/home/rezapish/Desktop/comp and raw/compressed"
# os.mkdir(rawPath)
# os.mkdir(compressedPath)
currentFiles = [] 
compressedFiles = []

os.chdir(rawPath)
while True: 
    sleep(5)
    currentFiles = [f for f in listdir(rawPath) if isfile(join(rawPath, f))]
    newFiles = []
    for file in currentFiles: 
        if file not in compressedFiles: 
            ZipFile(compressedPath + '/' + file + '.zip', 'w').write(file)
            compressedFiles.append(file)
    