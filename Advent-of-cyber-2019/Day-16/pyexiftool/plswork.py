import exiftool

files = ["/files"]
with exiftool.ExifTool() as et:
	metadata = et.get_metadata_batch(files)
for d in metadata:
	print(d)	