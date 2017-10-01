
from backup import zipFolder
from pathlib import Path

folderName = 'Test'
folderDir = str(Path.home())

zipFolder('Test',folderDir)