# script for ziping and backingup files on computer
#shebang line, read up

import shutil, os
from pathlib import Path

workingDir = str(Path.home()) + '\Desktop' #change for where the files should be copied
os.chdir(workingDir)

filesDir = (os.listdir()) #makes a list of all files
print(filesDir)

# shutil.copy('test.txt', 'C:\\Users\\arisa\\Documents\\test2.txt')		

# try/except around the whole code. Se --> sentex
# try

# except