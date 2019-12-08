#!/usr/bin/env python3
# updated : 01-15-2019

import argparse
import os
import sys
import urllib.request
try :
	from bs4 import BeautifulSoup
except ModuleNotFoundError :
	print("module bs4 not found")
	print("try : pip3 install bs4")
	exit()
try:
	from pytube import YouTube
except ModuleNotFoundError :
	print("module pytube not found")
	print("try : pip3 install pytube")
	exit()


does_path_exists = lambda path_variable : True if os.path.exists(path_variable) else False
does_file_exists = lambda file_path: True if os.path.isfile(file_path) else False

def get_playlist_url(playlist_url):
	'''
	return list of video's ulr in playlist_url
	'''

	result = []

	req = urllib.request.Request(playlist_url)
	response = urllib.request.urlopen(req)
	soup = BeautifulSoup(response, 'html.parser')

	for i in soup.find_all('a'):
		if 'watch' in i['href']:
			result.append(i['href'])

	result =  ['https://youtube.com' + i  for i in result]
	return set(result)

def DownloadVideo(url,path=os.getcwd()):
	'''
	main function used to download videos
	url : youtube url.
	path : download folder.
	'''

	print('[*] Connecting to youtube ....')
	myvideo = YouTube(url)

	# downloading the video
	print('Video Title : ', myvideo.title)
	print('[*] Downloading ...')

	mystream = myvideo.streams.first() # download with first quality in the list, not necessarly the best quality
	mystream.download(path)

	print('[+]FINISHED')



if __name__ == '__main__':

	download_folder = None
	video_url = None
	playlist_url = None
	file_path = None


	# getting args from command line
	parser = argparse.ArgumentParser(description='download videos from youtube')
	parser.add_argument('path', nargs=1, help='download folder')
	args_group = parser.add_mutually_exclusive_group(required=True)
	args_group.add_argument('-f', '--file', nargs=1, help='urls stored on file line by line')
	args_group.add_argument('-u', '--url', nargs=1, help='video url')
	args_group.add_argument('-play', '--playlist', nargs=1, help='youtube playlist url')
	args = parser.parse_args()


	# check validity of command line args
	if does_path_exists(args.path[0]):
		download_folder = args.path[0]
	else :
		print("download folder doesnt exists : {}".format(args.path[0]))
		exit()
	if args.file :
		if does_path_exists(args.file[0]):
			file_path = args.file[0]
		else :
			print("file doesnt exists : {}".format(args.file[0]))
			exit()
	if args.url :
		video_url = args.url[0]

	if args.playlist :
		playlist_url = args.playlist[0]


	# perform actions (downloading) based on user args
	if video_url :
		DownloadVideo(video_url, download_folder)
		exit()

	if playlist_url:
		print("retreiving urls from playlist ....")
		for video in get_playlist_url(playlist_url):
			try :
				DownloadVideo(video, download_folder)
			except :
				print("This video cannot be downloaded")
				pass
		exit()

	if file_path:
		with open(file_path) as file:
			for line in file:
				video = line.rstrip('\n')
				DownloadVideo(video, download_folder)

		exit()
