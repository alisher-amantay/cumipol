# imports
import urllib.request, urllib.parse
import json
with open('input.json', 'r') as infile:
    # Reading from json file
    loan_obj = json.load(infile)
data = json.dumps(loan_obj).encode()

req =  urllib.request.Request('http://127.0.0.1:8080', data=data) # POST data
resp = urllib.request.urlopen(req)

CUMIP = resp.read().decode() #Cumilative interest paid over a period is received
print('Cumilative interest paid over the period: ', CUMIP)
