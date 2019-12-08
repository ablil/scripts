#!/bin/bash
# description: Sign APKs
# author: _ablil
# date: 04-18-2019

# check root user and passed argument
if [[ "$(id -u)" != 0 ]] || [[ "$#" != 1 ]]; then
	echo "Run as root"
	echo "Usage: sudo ./$0 <apkfile.apk>"
	exit
else
	if [ ! -f "$1" ]; then
		echo "$1 NOT FOUND"
		exit
	fi
fi

# check apktool and openjdk-11-jdk-headless
apktool_status=$(dpkg -l | grep apktool)
openjdk_status=$(dpkg -l | grep openjdk)
if [[ -z "$apktool_status" ]] && [[ -z "$openjdk_status" ]]; then
	echo "Please install the following packages: "
	printf "\tapktool\n"
	printf "\topenjdk\t"
	exit
elif [ -z "$apktool_status" ]; then
	echo "Please install apktool"
	echo "sudo apt-get install apktool"
	exit
elif [ -z "$openjdk_status" ]; then
	echo "Please install openjdk"
	echo "sudo apt-get install openjdk"
	exit
else
	echo "Necessary packages are installed"
fi


# create the keystore
echo "[*] Creating keystore ..."
keytool -genkey -v -keystore /tmp/debug.keystore -storepass android -alias androiddebugkey -keypass android -keyalg RSA -keysize 2048 -validity 10000
if [ ! $? ]; then
	echo "Could NOT create keystore"
	echo "DO IT MANUALLY"
	exit
else
	echo "[+] Created keystore successfully /tmp/debug.keystore"
fi

# Sign the APK
echo "[*] Signing $1 ..."
jarsigner -verbose -keystore /tmp/debug.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA "$1" androiddebugkey
if [ ! $? ]; then
	echo "[-] Could NOT Sign the APK"
	exit
else
	echo "[+] $1 IS SIGNED GOOD TO GO"
fi

