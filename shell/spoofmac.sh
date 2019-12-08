#!/bin/bash
# description: change MAC address to Random 
# author: _ablil
# date: 04/18/2019

# Check root user
if [[ "$(id -u)" -ne 0 ]]; then
	echo "run script as Root"
	exit
fi

# check macchanger
if [[ ! "$(dpkg -l | grep -q macchanger)" ]]; then
	echo "Please install macchanger"
	echo "sudo apt-get install macchanger"
	exit
fi

# get wlan iface
interfaces=$(ls /sys/class/net)
for i in "${!interfaces[@]}"; do
	echo "  $i - ${interfaces[$i]}"
done
while 'true'; do
	read -r "Choose iface: " choice
	if [[ "$choice" -lt 0 ]] || [[ "$choice" -ge ${#interfaces[@]} ]]; then
		echo "Choose valid Number"
	else
		iface=${interfaces[$choice]}
		break
	fi
done

# Chaning mac address
sudo ifconfig "$iface" down

sudo macchanger -b -r "$iface" > /dev/null
if [ "$?" -ne 0 ]; then
	echo "Could NOT change mac address"
	sudo ifconfig "$iface" up
	exit
fi

sudo ifconfig "$iface" up

# Display the new mac address
sudo macchanger -s "$iface"
