from selenium import webdriver
import time
import pytest
import requests
import json

r = requests.get("https://merchant-staging.heropay.me/api/merchant/user/methods/100010044/17?channelId=desktop&method"
                 "=deposit&sessionId=0000-0000-0000-0000").text
#print(r)
p = json.loads(r)
p1 = p['methods'][0]
print(r)
print(p1['method'])
