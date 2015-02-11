#! /usr/bin/env python

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib
    from urllib import urlopen

import re
import sys

print("we will try to open this url, in order to get IP Address")

url = "http://checkip.dyndns.org"

print(url)

if sys.version_info.major == 3 :
    request = urlopen(url).read().decode('utf-8')
else:
    request = urlopen(url).read()

regxip = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}")


theIP = re.findall(regxip, request)

print("your IP Address is: ", theIP)
