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