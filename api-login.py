from unittest import result
import requests
import urllib3
urllib3.disable_warnings()


ip = 'api-turbonomic.aiops-spgi-22bfd3cd491bdeb5a0f661fb1e2b0c44-0000.eu-de.containers.appdomain.cloud'
username = 'administrator'
password = 'T3mporal!'

payload = {'username': username, 'password': password}
r = requests.post(f'https://{ip}/vmturbo/rest/login', data=payload, verify=False)
r.encoding = 'JSON'
token = r.headers['Set-Cookie'].split(';')[0]
print(token)
