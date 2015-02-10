
#! /usr/bin/env python

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

## python3 version

#import urllib.request
import re

print("we will try to open this url, in order to get IP Address")

url = "http://checkip.dyndns.org"

print(url)

request = urlopen(url).read().decode('utf-8')


regxip = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}")


theIP = re.findall(regxip, request)

print("your IP Address is: ",  theIP)
