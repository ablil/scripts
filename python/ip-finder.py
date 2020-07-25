#!/usr/bin/env python3
# updated : 01-14-2019

import sys
import json
import requests
import re

url = "https://tools.keycdn.com/geo.json?host="
usage = f"usage : python3 {sys.argv[0]} 105.42.108.231"

if __name__ == "__main__":

    # check argument count
    if len(sys.argv) != 2:
        print(usage)
        sys.exit(-1)

    # check help menu
    if sys.argv[1] in ("-h", "--help"):
        print(usage)
        sys.exit(0)

    # check if IP is valid or not & set url
    if not re.match(r"^(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.)){3}(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))$", sys.argv[1]):
        print("Invalid IP Address")
        sys.exit(1)
    else:
        splited = sys.argv[1].split('.')
        for part in splited:
            if not int(part) in range(1, 255):
                print("Invalid IP Address")
                sys.exit(2);

    # get respone from url API
    request_url = url + str(sys.argv[1])
    response = requests.get(request_url)
    json_data = response.json()  # transform to json format

    if json_data["status"] == "success":

        # setting variable to display
        host = "host : {}".format(json_data["data"]["geo"]["host"])
        ip = "IP : {}".format(json_data["data"]["geo"]["ip"])
        rdns = "rdns : {}".format(json_data["data"]["geo"]["rdns"])
        asn = "asn : {}".format(json_data["data"]["geo"]["asn"])
        isp = "ISP : {}".format(json_data["data"]["geo"]["isp"])
        country_name = "country name : {}".format(
            json_data["data"]["geo"]["country_name"]
        )
        country_code = "country code : {}".format(
            json_data["data"]["geo"]["country_code"]
        )
        region_name = "region name : {}".format(json_data["data"]["geo"]["region_name"])
        region_code = "region code : {}".format(json_data["data"]["geo"]["region_code"])
        city = "city : {}".format(json_data["data"]["geo"]["city"])
        postal_code = "postal code : {}".format(json_data["data"]["geo"]["postal_code"])
        continent_name = "continent name : {}".format(
            json_data["data"]["geo"]["continent_name"]
        )
        continent_code = "continent code : {}".format(
            json_data["data"]["geo"]["continent_code"]
        )
        latitude = "latitude : {}".format(json_data["data"]["geo"]["latitude"])
        longitude = "longitude : {}".format(json_data["data"]["geo"]["longitude"])
        metro_code = "metro code : {}".format(json_data["data"]["geo"]["metro_code"])
        timezone = "timezone : {}".format(json_data["data"]["geo"]["timezone"])
        datetime = "datetime : {}".format(json_data["data"]["geo"]["datetime"])

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
    else:
        print("error occured while receiving data !!!")
