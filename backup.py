# script for ziping and backingup files on computer
#shebang line, read up

import shutil, os
from pathlib import Path
import zipfile
from send2trash import send2trash

def zipFolder(folderName,folderLocation):
	workingDir = folderLocation + '\\' + folderName #change for where the files should be copied
	os.chdir(workingDir)

	fileList = os.listdir()

	newZip = zipfile.ZipFile(folderName+'_Copy.zip','w')
	for file in fileList:
		newZip.write(file, compress_type=zipfile.ZIP_DEFLATED)
	newZip.close()

	zipPath = str(Path.home())+'\\'+folderName+'_Copy.zip'

	if(os.path.exists(zipPath)):
		send2trash(zipPath)

	shutil.move(folderName+'_Copy.zip',folderLocation)