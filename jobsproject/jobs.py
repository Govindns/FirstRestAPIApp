import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/pune/'
r=requests.get(BASE_URL+ENDPOINT)
data=r.json()
for job in data:
    print('id:',job['id'])
    print('Date:',job['date'])
    print('Company Name:', job['company'])
    print('Title:', job['title'])
    print('Address:', job['address'])
    print('Email:', job['email'])
    print('Phone Number:', job['phonenumber'])
    print()