# Black Hat Python Scripts :tophat:

:warning: These scripts are slightly different from the one on the book, because I optimized them for my needs.
Also they are written in Python3 not Python2

## Chapter Two : The Network Basics
Empty For Now

## Chapter Three : The Network Raw Sockets And Sniffing
* sniffer.py : Sniff one packet with sockt module.
* sniffer_ip_hader_decode : Sniff and decode IP header.
* sniffer_with_icmp.py : Sniff and decode IP/ICMP headers.
* scanner.py : Host discovery using UDP packets. (Receive ICMP when UDP port is closed, none otherwise)

## Chapter Four : Owning the Network with Scapy
* mail_sniffer.py : Simple mail sniffer. (Only unencrypted ports)
* arper.py : Poison tarfic between host and gateway, sniff packet and store them in pcap file. (*ARP poisoning*)

## Chapter Five : Web Hackery
* web_app_mapper.py : Check WebApp urls (opensource one such as wordpress, joomla ...)
* content_bruter.py : WebApp content bruteforcer.
* joomla_killer.py : joomla web form brute forcer using wordlist of passwords.
