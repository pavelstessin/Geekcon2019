#!/usr/bin/env python3
'''
-------------------------------------------------------------------------
File name    : talk_to_remote_server.py
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


def get_project_name():
    url = 'http://192.168.43.31:9000/get_project_name'
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    return r.data


