# script for ziping and backingup files on computer
#shebang line, read up

import shutil, os
from pathlib import Path
import send2trash

workingDir = str(Path.home()) + '\Test' #change for where the files should be copied
os.chdir(workingDir)

print(workingDir)

if os.path.exists(workingDir+'_Copy'):
	send2trash.send2trash(workingDir+'_Copy')
	
shutil.copytree(workingDir,workingDir+'_Copy')

# try/except around the whole code. Se --> sentex
# try

# except