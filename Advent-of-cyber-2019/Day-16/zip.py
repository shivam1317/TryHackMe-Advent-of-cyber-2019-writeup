import zipfile
with zipfile.ZipFile('final-final-compressed.zip','r') as zip_ref:
	zip_ref.extractall('extracted')