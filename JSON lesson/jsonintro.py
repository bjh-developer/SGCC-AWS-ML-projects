import json
import pprint as pp

about_me = {
    'name' : 'Joon Hao',
    'age' : 16,
    'gender' : 'male',
    'hobby' : 'coding'
}

print('----original----')
print(about_me)
pp.pp(about_me)

print('')

#json.dumps() method
to_json = json.dumps(about_me)
print(to_json)

#change from json to dictionary
to_dict = json.loads(to_json)
print(to_dict)