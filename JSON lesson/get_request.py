import json
import requests

r = requests.get('https://reqres.in/api/users/2')

# print(r)
# print(type(r))
# print(r.status_code)
# print(r.text)
# print(r.headers)
# print(r.url)

#method 1 - using json library
# response = r.text
# response_dict = json.loads(response)

#method 2 - built in json.json() function
# response_dict2 = r.json()

#demonstration of programmatic access to an API
people = {} #an empty dictionary to store extracted info
for page in range(1, 3):
    r = requests.get('https://reqres.in/api/users?page=2')

    data = r.json()['data']

    for user in data:
        people[user['id']] = user['email']
print(people)


print('--------------------------------')
payload = {
    'name' : 'Spongebob',
    'job' : 'Cook'
}

r = requests.post('https://reqres.in/api/users', data=payload)
print(r.status_code)
print('User has been created')
print(r.text)