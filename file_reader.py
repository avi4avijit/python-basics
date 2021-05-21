"""

This python module will read all '.txt' files in a directory.

"""
# Import Module
import os

# Folder Path "Enter Folder Path (local)"
path = "C:/pytest"

# Change the directory
os.chdir(path)


# Read text File
def read_text_file(file_path):
	with open(file_path, 'r') as f:
		print(f.read())


# main
def main():

	# iterate through all file
	for file in os.listdir():
		# Check whether file is in text format or not
		if file.endswith(".txt"):
			file_path = f"{path}\{file}"

			# call read text file function
			read_text_file(file_path)


if __name__ == "__main__":
	main()

