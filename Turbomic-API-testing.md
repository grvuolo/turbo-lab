swagger/external/index.html


curl -X 'GET' \
  'https://api-turbonomic.aiops-spgi-22bfd3cd491bdeb5a0f661fb1e2b0c44-0000.eu-de.containers.appdomain.cloud/api/v3/users' \
  -H 'accept: application/json' -k
  
  
  
  
  curl -X POST -H " https://pi-turbonomic.aiops-spgi-22bfd3cd491bdeb5a0f661fb1e2b0c44-0000.eu-de.containers.appdomain.cloud/vmturbo/rest/login --header 'Authorization: apiToken _ZABlyxnT3mpC9xjVDW5MQ' -k


curl -X POST -H 'Authorization: Basic YWRtaW5pc3RyYXRvcjpUM21wb3JhbCE=' https://api-turbonomic.aiops-spgi-22bfd3cd491bdeb5a0f661fb1e2b0c44-0000.eu-de.containers.appdomain.cloud/vmturbo/rest/login -k


YXBpLWNhbGxlcjpUM21wb3JhbCE=


curl -X POST -u 'username:password' https://api-turbonomic.aiops-spgi-22bfd3cd491bdeb5a0f661fb1e2b0c44-0000.eu-de.containers.appdomain.cloud/vmturbo/rest/login -k


administrator:T3mporal!


## Get JSESSIONID

Fails authentication
```
JSESSIONID=$(curl \
    --silent \
    --cookie-jar - \
    --insecure \
    https://api-turbonomic.aiops-spgi-22bfd3cd491bdeb5a0f661fb1e2b0c44-0000.eu-de.containers.appdomain.cloud/vmturbo/rest/login \
    --data "username=administrator&password=T3mporal!" \
    | awk '/JSESSIONID/{print $7}')
```


Use python to get JSESSIONID

vi api-login.py 

```
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
~              
```

```
python3 api-login.py
JSESSIONID=node01b2wvjzl4s8vv145cvzwnp2hkw245.node0
``




var express = require('express');
var multer  = require('multer');
var app = express();

app.configure(function(){
  app.set('port', process.env.PORT || 3000);
  app.use(multer());
});

app.post('/', function (req, res) {
  var from = req.body.from;
  var text = req.body.text;
});

var server = app.listen(app.get('port'), function() {
  console.log('Listening on port %d', server.address().port);
});
~                                                                                                                                                
~                                                                                                                                                
~               