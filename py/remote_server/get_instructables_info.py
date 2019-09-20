#!/usr/bin/env python3
'''
-------------------------------------------------------------------------
File name    : get_instructables_info.py
Title        :
Project      :
Developers   :  Doron
Created      : Thu Sep 19, 2019  09:39
Description  :
Notes        :
---------------------------------------------------------------------------
---------------------------------------------------------------------------*/
'''
# import os
# import json

# output = os.popen("wget --quiet --method GET --header 'x-rapidapi-host: devru-instructables.p.rapidapi.com' --header 'x-rapidapi-key: 481fd00a6fmsha8a2edd15ad2907p197263jsnedc5723cd27f' --output-document - https://devru-instructables.p.rapidapi.com/json-api/getCategories")
# output_json = json.loads("".join(output.readlines()))
# import pdb; pdb.set_trace()  # XXX BREAKPOINT
# print(output_json)
import requests

# url = "https://devru-instructables.p.rapidapi.com/json-api/getCategories"

# headers = {
    # 'x-rapidapi-host': "devru-instructables.p.rapidapi.com",
    # 'x-rapidapi-key': "481fd00a6fmsha8a2edd15ad2907p197263jsnedc5723cd27f"
    # }

# response = requests.request("GET", url, headers=headers)

# print(response.text)
# url = "https://devru-instructables.p.rapidapi.com/json-api/showInstructable"

# # querystring = {"id":"EBUFWEJHWJJWSD0"}
# querystring = {"id":"EBNQUFIFIHVM2IS"}

# headers = {
    # 'x-rapidapi-host': "devru-instructables.p.rapidapi.com",
    # 'x-rapidapi-key': "481fd00a6fmsha8a2edd15ad2907p197263jsnedc5723cd27f"
    # }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print([i for i in response.text.split("\n") if "title" in i])

url = "https://devru-instructables.p.rapidapi.com/list"

querystring = {"type":"title","limit":"2"}

headers = {
    'x-rapidapi-host': "devru-instructables.p.rapidapi.com",
    'x-rapidapi-key': "481fd00a6fmsha8a2edd15ad2907p197263jsnedc5723cd27f"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
