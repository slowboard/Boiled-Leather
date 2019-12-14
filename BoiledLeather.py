import os, re, shutil, sys, fileinput

book = ["AFFC","ADWD"]			# The book names. Don't change these
start = [0,0]					# The number of the prologue .html files
								# AFFC prologue is in chapter000.html
								# ADWD prologue is in chapter000.html

og_file = "chapter"				# Original filename. Enter all letters before the enumeration.

padding = 3						# number of padded zeros
length = [46, 73]				# Number of chapters in each book
								# AFFC chapter000.html to chapter045.html
								# ADWD chapter000.html to chapter072.html

path = os.getcwd()				# Gets the path to the work folder (where this script is)
outfolder = "%s/book/" % path	# Generates path to the output folder



# Getting a list of the chapters
f = open("%s/chapters.txt" % path)
s = f.read()

chapters = []
string = re.split(":|\n",s)

for i in string:
	if "ADWD" in i or "AFFC" in i:
		chapters.append(i[1:])


# Copying and renaming files
for index, bookname in enumerate(book):

	# Folder name for original files
	folder = "%s/%s/" % (path,bookname)

	# Copying and renaming chapters
	for i in range(start[index],start[index]+length[index]):
		# Getting original filename
		num = str(i).zfill(padding)
		og_filename = "%s%s%s.html" % (folder, og_file, num)

		# new filename
		temp_name = "%s%s %d.html" % (outfolder, bookname, i-start[index]+1)
		shutil.copy(og_filename,temp_name)


# Renaming chapters to fit boiled leather semi-chronological order
for num, name in enumerate(chapters):
	filename = "%s%s.html" % (outfolder, name)
	newfile = "%s%d - %s.html" % (outfolder, num+1, name)
	os.rename(filename,newfile)



# Things that don't really work or I don't use
# Part of the main for loop, for moving the appendix. Does work, but I don't use it
# appendix = book[1]
# app_start = 78
# app_stop = 99
	# Copying and moving appendecies
	# if bookname == appendix:
	# 	for i in range(app_start,app_stop+1):
	# 		og_filename = "%s%s_%03d.html" % (folder, og_file, i)

	# 		temp_name = "%sappendix %d.html" % (outfolder, i-app_start+1)
	# 		shutil.copy(og_filename,temp_name)

# Renaming stylesheets for use of two seperate stylesheets. Doesn't work.
# for i in range(stop[1]-start[1]):
# 	searchExp = """  <link href="styles/stylesheet.css" rel="stylesheet" type="text/css"/>"""
# 	replaceExp = """  <link href="styles/stylesheet1.css" rel="stylesheet" type="text/css"/>"""
# 	name = "%s%s %d.html" % (outfolder, book[1], i)
# 	for line in fileinput.input(name, inplace = 1):
# 		if searchExp in line:
# 			line = line.replace(searchExp,replaceExp)
