import os 
import zipfile

zipfiles = os.listdir('extracted')
for f in zipfiles:
	with zipfile.ZipFile('extracted/'+f,'r') as zip_ref:
		zip_ref.extractall('files')