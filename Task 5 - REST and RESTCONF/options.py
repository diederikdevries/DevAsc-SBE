#!/usr/bin/python3.8

# curl -i -k -X "OPTIONS" \
# "https://192.168.56.101:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity" \
# -H 'Accept: application/yang-data+json' \
# -u 'cisco:cisco123!'

#'Accept: application/yang-data+json'
#headers = {'Accept': 'application/yang-data+json'}

import requests
r=requests.options('https://192.168.56.101:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity', headers = {'Accept': 'application/yang-data+json'}, verify=False,auth=('cisco','cisco123!'))
print(r.headers)