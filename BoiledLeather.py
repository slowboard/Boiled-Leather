# The script assumes that the files for each book is in separate subfolders the folder this script is in.
# So if the script is at "C:\Users\YourUserName\Download\boiled_leather.py", then the script assumes the
# book files are in "C:\Users\YourUserName\Download\AFFC" and "C:\Users\YourUserName\Download\ADWD".

# This script also assumes the files follow the format:
# {original_file_prefix}{chapter_number_with_padding}.{file_extension}
# 
# For me, the files are called "index_split_xxx.html", so the variables should be:
original_file_prefix = "index_split_"
original_file_extension = "html"
padding = 3

# The script also assumes that there might be a number of pre-amble files.
# So the book starts at a number other than 1. In my case, the AFFC prologue
# is "index_split_007.html", and the ADWD prologue is "index_split_005.html"
# Therefore the prologue_counts is 7 and 5:
prologue_counts = [7,5]

# The output files will be placed in the subfolder "book", with the following format:
# "{boiled_leather_chapter_number} - {original_chapter}.{file_extension}"
# For example: "Jaime I" is the AFFC chapter 9, and boiled leather chapter 17, so it will be named
# "17 - AFFC 9.{file_extension}"

import shutil
import pathlib

books = ["AFFC", "ADWD"] # The book names
chapter_count = [46, 73] # Number of chapters in each book

script_path = pathlib.Path(__file__)
cwd = script_path.parent
output_folder = cwd / 'book' 
if not output_folder.exists():
    output_folder.mkdir()


# Getting a list of the chapters. They are in the format "{Chapter name}: {Book} {chapter number}"
# We only want the "{Book} {chapter number}" part
chapters = []
with open(cwd / 'chapters.txt', 'r', encoding='utf-8') as f:
    file_contents = f.read()
    for line in file_contents.split('\n'):
        title, book_and_chapter_number = line.split(': ')
        chapters.append(book_and_chapter_number)


# Copying and renaming files
for book_index, book_name in enumerate(books):

    # Folder name for original files
    folder = cwd / book_name

    # Start and end number for the files of the book
    book_start_number = prologue_counts[book_index]
    book_end_number = book_start_number + chapter_count[book_index]

    # Copying and renaming chapters
    for i in range(book_start_number, book_end_number):

        # Getting file number, with padding
        file_number = str(i).zfill(padding)
        original_filename = folder / f"{original_file_prefix}{file_number}.{original_file_extension}"

        # new filename
        new_chapter_number = i + 1 - prologue_counts[book_index]
        temp_name = output_folder / f"{book_name} {new_chapter_number}.{original_file_extension}"
        shutil.copy(original_filename, temp_name)


# Renaming chapters to fit boiled leather semi-chronological order
for num, name in enumerate(chapters):
    current_filename = output_folder / f"{name}.{original_file_extension}"
    new_filename = output_folder / f"{num+1} - {name}.{original_file_extension}"
    current_filename.rename(new_filename)

