#!/usr/bin/env python3
'''
-------------------------------------------------------------------------
File name    : talk_to_server.py
Title        : 
Project      : 
Developers   :  doron
Created      : Fri Sep 20, 2019  09:46pm
Description  : 
Notes        : 
---------------------------------------------------------------------------
---------------------------------------------------------------------------*/
'''
import requests
import json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}
 
r = requests.post(url, data=json.dumps(payload), headers=headers)




