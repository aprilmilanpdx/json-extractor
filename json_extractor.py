import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

file_name = input('Enter file name: ')
webUrl = urllib.request.urlopen(file_name)
data = webUrl.read()

info = json.loads(data)
comments = info["comments"]

total_count = 0
for item in comments:
  total_count += item["count"]
print(total_count)