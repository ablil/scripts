#!/usr/bin/env python3
# updated : 01-14-2019

'''
windows lack this command for calculating md5sum of file
this scripts do the job for you
'''

import hashlib
import sys

if __name__ == '__main__':
	hash_func = hashlib.md5()
	usage = "usage : python3 md5su.py filename.txt"

	# add help menu
	if len(sys.argv) == 2 and sys.argv[1] in ('-h', '--help'):
		print(usage)
		exit()

	try :
		filename = sys.argv[1]

		# open file and read data
		file = open(filename, 'rb')
		data = file.read()
		file.close()

		# get checksum
		hash_func.update(data)
		print(hash_func.hexdigest(), ' ', filename)
	except IndexError:
		print(usage)
		exit()
	except FileNotFoundError:
		print('FILE NOT FOUND')
		print(usage)
		exit()
	except Exception as e:
		raise e