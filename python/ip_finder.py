#!/usr/bin/env python3
# updated : 01-14-2019

import sys
import json
import requests
from is_ipv4 import is_ipv4


url = 'https://tools.keycdn.com/geo.json?host='
usage = "usage : python3 ip_finder.py 105.42.108.231"

if __name__ == '__main__':
    
    # add help menu
    if len(sys.argv) == 2 and sys.argv[1] in ('-h', '--help'):
        print(usage)
        exit()

    # check if IP is valid or not & set url 
    try :
        if not is_ipv4(sys.argv[1]) :
            print("invalid ip address !!!")
            exit()
        final_url = url + str(sys.argv[1])
    except IndexError:
        print(usage)
        exit()
    except Exception as e:
        raise e

    # get respone from url API
    response = requests.get(final_url)
    json_data = response.json() # transform to json format

    if json_data['status'] ==  'success':

        # setting variable to display 
        host = 'host : {}'.format(json_data['data']['geo']['host'])
        ip = 'IP : {}'.format(json_data['data']['geo']['ip'])
        rdns = 'rdns : {}'.format(json_data['data']['geo']['rdns'])
        asn = 'asn : {}'.format(json_data['data']['geo']['asn'])
        isp = 'ISP : {}'.format(json_data['data']['geo']['isp'])
        country_name = 'country name : {}'.format(json_data['data']['geo']['country_name'])
        country_code = 'country code : {}'.format(json_data['data']['geo']['country_code'])
        region_name = 'region name : {}'.format(json_data['data']['geo']['region_name'])
        region_code = 'region code : {}'.format(json_data['data']['geo']['region_code'])
        city = 'city : {}'.format(json_data['data']['geo']['city'])
        postal_code = 'postal code : {}'.format(json_data['data']['geo']['postal_code'])
        continent_name = 'continent name : {}'.format(json_data['data']['geo']['continent_name'])
        continent_code = 'continent code : {}'.format(json_data['data']['geo']['continent_code'])
        latitude = 'latitude : {}'.format(json_data['data']['geo']['latitude'])
        longitude = 'longitude : {}'.format(json_data['data']['geo']['longitude'])
        metro_code = 'metro code : {}'.format(json_data['data']['geo']['metro_code'])
        timezone = 'timezone : {}'.format(json_data['data']['geo']['timezone'])
        datetime = 'datetime : {}'.format(json_data['data']['geo']['datetime'])

        # display data
        print(host)
        print(ip)
        print(rdns)
        print(asn)
        print(isp)
        print(country_name)
        print(country_code)
        print(region_name)
        print(region_code)
        print(city)
        print(postal_code)
        print(continent_name)
        print(continent_code)
        print(latitude)
        print(longitude)
        print(metro_code)
        print(timezone)
        print(datetime)
    else :
        print("error occured while receiving data !!!")