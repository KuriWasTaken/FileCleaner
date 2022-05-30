from os import walk
import os
import pathlib
import shutil 
  
scriptName = "FileCleaner.py" #The name of the script

filePath = input("Enter file path, Enter blank for current directory: ")

filenames = []

if filePath == "":
    filenames = next(walk(pathlib.Path().resolve()), (None, None, []))[2]
else:
    filenames = next(walk(filePath), (None, None, []))[2]

def arrayFind(array, str):
    for i in array:
        if "."+i in str:
            return True
    return False


programingExtensions = ["py", "lua", "c", "h", "cpp", "js"]
pictureExtensions = ["png", "jpg", "webp", "pdn", "jpeg", "gif", "tiff", "psd", "pdf", "eps", "ai", "indd", "raw"]
zippedExtensions = ["rar", "zip"]

programingDirectory = ""
documentDirectory = ""
pictureDirectory = ""
zippedDirectory = ""
urlDirectory = ""


folders = [False, False, False, False, False] #0 = Programin. 1 = Documents. 2 = Images, 3 = Zipped. 4 = Url File.



for i in filenames:
    if i != scriptName:
        if arrayFind(programingExtensions, i):
            if folders[0] == False:
                os.makedirs(str(pathlib.Path().resolve()) + "/" + filePath + "/Programing")
                folders[0] = True
                programingDirectory = str(pathlib.Path().resolve()) + "/" + filePath + "/Programing"
            shutil.move(str(pathlib.Path().resolve()) + "/" + filePath + "/" + i, str(pathlib.Path().resolve()) + "/" + filePath + "/Programing") 
        elif ".txt" in i:
            if folders[1] == False:
                os.makedirs(str(pathlib.Path().resolve()) + "/" + filePath + "/Documents")
                folders[1] = True
                documentDirectory = str(pathlib.Path().resolve()) + "/" + filePath + "/Documents"
            shutil.move(str(pathlib.Path().resolve()) + "/" + filePath + "/" + i, str(pathlib.Path().resolve()) + "/" + filePath + "/Documents") 
        elif arrayFind(pictureExtensions, i):
            if folders[2] == False:
                os.makedirs(str(pathlib.Path().resolve()) + "/" + filePath + "/Pictures")
                folders[2] = True
                pictureDirectory = str(pathlib.Path().resolve()) + "/" + filePath + "/Pictures"
            shutil.move(str(pathlib.Path().resolve()) + "/" + filePath + "/" + i, str(pathlib.Path().resolve()) + "/" + filePath + "/Pictures")
        elif arrayFind(zippedExtensions, i):
            if folders[3] == False:
                os.makedirs(str(pathlib.Path().resolve()) + "/" + filePath + "/ZippedFolders")
                folders[3] = True
                zippedDirectory = str(pathlib.Path().resolve()) + "/" + filePath + "/ZippedFolders"
            shutil.move(str(pathlib.Path().resolve()) + "/" + filePath + "/" + i, str(pathlib.Path().resolve()) + "/" + filePath + "/ZippedFolders")
        elif ".url" in i:
            if folders[4] == False:
                os.makedirs(str(pathlib.Path().resolve()) + "/" + filePath + "/Shortcuts")
                folders[4] = True
                urlDirectory = str(pathlib.Path().resolve()) + "/" + filePath + "/Shortcuts"
            shutil.move(str(pathlib.Path().resolve()) + "/" + filePath + "/" + i, str(pathlib.Path().resolve()) + "/" + filePath + "/Shortcuts") 
os.makedirs(str(pathlib.Path().resolve()) + "/" + filePath + "/MISCFILES")
subdirs = [x[0] for x in os.walk('.')]
for i in subdirs:
    if i != ".":
        filenamesSub = next(walk(i), (None, None, []))[2]
        for v in filenamesSub:
            if v != scriptName:
                if arrayFind(programingExtensions, v):
                    shutil.move(str(pathlib.Path().resolve()) + "\\" + i, programingDirectory) 
                    break
                elif ".txt" in i:
                    shutil.move(str(pathlib.Path().resolve()) + "\\"  + i, documentDirectory) 
                    break
                elif arrayFind(pictureExtensions, v):
                    shutil.move(str(pathlib.Path().resolve()) + "\\"  + i, pictureDirectory)
                    break
                elif arrayFind(zippedExtensions, v):
                    shutil.move(str(pathlib.Path().resolve()) + "\\"  + i, zippedDirectory)
                    break
                elif ".url" in i:
                    shutil.move(str(pathlib.Path().resolve()) + "\\"  + i, urlDirectory)
                    break
                else:
                    shutil.move(str(str(pathlib.Path().resolve()) + "\\"  + i, str(pathlib.Path().resolve()) + "/" + filePath + "/MISCFILES"))
                    break

print("Done!")
