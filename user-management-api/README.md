# User Management through API

## Get Cookie

Authentication for interacting with API is through cookies. So first thing is to get the cookies

```
curl -s -k -c cookies -H 'accept: application/json' 'https://<turbo-url>/api/v3/login?hateoas=true' -d 'username=<username>&password=<password>'
```

Use the cookies file to execute the curls

-b cookie


## Get Users

```
curl -k -X 'GET' -b cookies 'https://<turbo-url>/api/v3/users' |  python -mjson.tool

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1180    0  1180    0     0   3751      0 --:--:-- --:--:-- --:--:--  3757
[
    {
        "uuid": "4303112158528",
        "displayName": "administrator",
        "username": "administrator",
        "roles": [
            {
.
.
.
```

## Get User Groups

Get Group info

```
curl -k -X 'GET' -b cookies 'https://<turbo-url>/api/v3/users/ldap/groups' |  python -mjson.tool

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   716    0   716    0     0   1088      0 --:--:-- --:--:-- --:--:--  1088
[
    {
        "uuid": "administrator",
        "displayName": "administrator",
        "type": "DedicatedCustomer",
        "roleName": "ADMINISTRATOR"
    },
    {
.
.
.
```


## Create new User

Use info from Group and Users requested to create a new user definition

vi create-user.json

```
{
  "displayName": "spgi-pot-auto-2",
  "username": "spgi-pot-auto-2",
  "password": "spgi-pot",
  "roles": [
    {
      "uuid": "automator",
      "displayName": "automator",
      "name": "AUTOMATOR"
    }
  ],
  "loginProvider": "Local",
  "type": "DedicatedCustomer",
  "showSharedUserSC": false
}
```

```
curl -X POST -b cookies -H "Content-Type: application/json" -d @/<path-to-file>/create-user.json 'https://<turbo-url>/api/v3/users' -k |  python -mjson.tool

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   525    0   237  100   288    363    442 --:--:-- --:--:-- --:--:--   805
{
    "uuid": "4466285621136",
    "displayName": "spgi-pot-auto-2",
    "username": "spgi-pot-auto-2",
    "roles": [
        {
            "uuid": "automator",
            "displayName": "automator",
            "name": "AUTOMATOR"
        }
    ],
    "loginProvider": "Local",
    "type": "DedicatedCustomer",
    "showSharedUserSC": false
}

```

## Delete Users

```
curl -k -X 'DELETE' -b cookies 'https://<turbo-url>/api/v3/users/4466285621136' |  python -mjson.tool

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:--  0:00:06 --:--:--     0
Expecting value: line 1 column 1 (char 0)
```