## Q.1 How many files did you extract(excluding all the .zip files)

--> so i made this script for unzipping the downloaded file 

```py
import zipfile
with zipfile.ZipFile('final-final-compressed.zip','r') as zip_ref:
	zip_ref.extractall('extracted')
```

--> after that i got many zip files in the extracted folder 

![[Pasted image 20210812132950.png]]

--> so we have to unzip these files also 

--> so i made one script for this 

```py
import os 
import zipfile

zipfiles = os.listdir('extracted')
for f in zipfiles:
	with zipfile.ZipFile('extracted/'+f,'r') as zip_ref:
		zip_ref.extractall('files')
```

--> and i got many text files in the `files` directory

--> so we have to count these all files so Let's make script for this also !

```py
import os
txtfiles = os.listdir('files')
count = 0

for t in txtfiles:
	count = count + 1	

print(count)
```

--> and i got answer as `50`

-------

## Q.2 How many files contain Version: 1.1 in their metadata?

--> for reading metadata we have to install pyexiftool module

--> after doing that i made one script for reading all metadata 

```py
import exiftool

files = ["/home/kali/Documents/THM/Advent-of-cyber-2019/Day-16/files"]
with exiftool.ExifTool() as et:
	metadata = et.get_metadata_batch(files)
for d in metadata:
	print(d)	
```

--> and i got metadata for every file and then i found `3` files which contains the word `version 1.1`

![[Pasted image 20210812130834.png]]

-----

## Q.3 Which file contains the password?

--> i simply run the grep command 

```c
grep -r "password"
```

--> and i found the password !

![[Pasted image 20210812134042.png]]

--> i also made one script for this but it didn't work i don't know why :(

```py
import os 
txtfiles = os.listdir('files')

for f in txtfiles:
	with open('files/'+f,'r') as reader:
		read = reader.readlines()
		for line in read:
			new_line = line.strip('\n')
			if "password" in new_line:
				print(new_line)
		# print(read)
```		