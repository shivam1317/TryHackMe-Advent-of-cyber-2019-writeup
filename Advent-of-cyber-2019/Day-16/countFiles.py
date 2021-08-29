import os
txtfiles = os.listdir('files')
count = 0

for t in txtfiles:
	count = count + 1	

print(count)