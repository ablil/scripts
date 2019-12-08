#!/usr/bin/env python3
# updated : 01-15-2019

import json
import requests

if __name__ == '__main__':
	url = 'http://ip-api.com/json'

	print("[*] resolving IP address ...")
	response = requests.get(url)
	json_data = response.json()

	# print data to user
	city = json_data['city']
	country = json_data['country']
	country_code = json_data['countryCode']
	isp = json_data['isp']
	latitude = json_data['lat']
	longitude = json_data['lon']
	organisation = json_data['org']
	query = json_data['query'] # IP ADDRESS
	region = json_data['region']
	region_name = json_data['regionName']
	timezone = json_data['timezone']

	print('city : ', city)
	print('country : ', country)
	print('country code : ', country_code)
	print('ISP : ', isp)
	print('latitude : ', latitude)
	print('longitude : ', longitude)
	print('org : ', organisation)
	print('IP : ', query)
	print('region : ', region)
	print('region name : ', region_name)
	print('timezone : ', timezone)
