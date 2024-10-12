import json

emp = {
    'name':'Jerry',
    'age':35,
    'salary':1000.0,
    'isMarried':True
}

json_string=json.dumps(emp, indent=4, sort_keys= True)
print(json_string)