import exiftool

files = ["/home/kali/Documents/THM/Advent-of-cyber-2019/Day-16/files"]
with exiftool.ExifTool() as et:
	metadata = et.get_metadata_batch(files)
for d in metadata:
	print(d)	