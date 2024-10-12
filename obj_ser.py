import json

emp = {
    'name':'Jerry',
    'age':35,
    'salary':1000.0,
    'isMarried':True
}

json_string=json.dumps(emp, indent=4)
print(json_string)