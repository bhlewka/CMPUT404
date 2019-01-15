import requests

r = requests.get('https://raw.githubusercontent.com/bhlewka/CMPUT404/master/lab1/requestsVersion.py')
code = r.content.decode('UTF-8').splitlines()

for c in code:
	print(c)
