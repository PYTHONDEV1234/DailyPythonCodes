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

with open('sort.json','w') as file:
    # json.dump(data , file, sort_keys=False, indent=4)
    json.dump(data , file, sort_keys=True, indent=4)

