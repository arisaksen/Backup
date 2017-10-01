# script for ziping and backingup files on computer
#shebang line, read up

import shutil, os
from pathlib import Path
import zipfile
import send2trash

folderName = 'Test'

workingDir = str(Path.home()) + '\\' + folderName #change for where the files should be copied
os.chdir(workingDir)
copyDir = workingDir+'_Copy'

print(workingDir)

if os.path.exists(copyDir):
	send2trash.send2trash(copyDir)
	
shutil.copytree(workingDir,copyDir)

print(Path.home())

# newZip = zipfile.ZipFile(folderName+'_Copy.zip','w')
# newZip.write(folderName+'_Copy', compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()

# try/except around the whole code. Se --> sentex
# try

# except