

## python3 version

import urllib.request
import re

print("we will try to open this url, in order to get IP Address")

url = "http://checkip.dyndns.org"

print(url)

request = urllib.request.urlopen(url).read()

print(request)
print("")
print("")
findip = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}")


theIP = re.findall(findip, request,1)

print("your IP Address is: ",  theIP)
