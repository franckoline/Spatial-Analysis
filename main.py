from camelcase import CamelCase
import requests


c = CamelCase()
s = 'this is my girl'
print(c.hump(s))
resp = requests.get('https://franckoline.com.ng')
print(resp)
