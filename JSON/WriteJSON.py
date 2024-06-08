import json

data = {
    "name":"Arvinder",
    "Age":34,
    "City":"Sirsa",
    "ID": 1234,
    "Weight": 78.46
}
with  open('Write.Json','w') as file :
    json.dump(data, file)