#!/usr/bin/python3.8

# curl -i -k -X "OPTIONS" \
# "https://192.168.56.101:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity" \
# -H 'Accept: application/yang-data+json' \
# -u 'cisco:cisco123!'

#'Accept: application/yang-data+json'
#headers = {'Accept': 'application/yang-data+json'}

# Everything,but now with data added :)
# Does need the logging monitor:
# ena, conf t, logging monitor

rheader= {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
rauth = ('cisco','cisco123!')
rdata = '{ "severity": "alerts" }'


import requests
r=requests.post('https://192.168.56.101:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor', 
verify=False,
headers = rheader, 
auth=rauth,
data=rdata)

print (r)
print(r.headers)