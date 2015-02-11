__author__ = 'rickei'
try :
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen

url = "http://myexternalip.com/raw"

print("checking from : " + url)

myip = urlopen(url).read().decode()
print(myip)