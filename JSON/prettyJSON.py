import json

data= {
    "name":"Arvinder",
    "Age": 45,
    "Languages":{
        "Primary":"Hindi",
        "Secondary":"English"
    },
    "Phone":"1234567890"
}
with open('pretty.json', 'w') as file :
    json.dump(data , file, indent=4)
    # json.dump(data , file)

