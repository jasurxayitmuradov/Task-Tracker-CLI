import json
json_string  = ''' 
{
    "tasks":[
        {
            "id":1,
            "name":"Do shopping"
        }
    ]
}
'''
data = json.loads(json_string)
print(data['tasks'])


