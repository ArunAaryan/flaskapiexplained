import requests
user = input("enter username")
r = requests.get('http://127.0.0.1:5000/show?name={}'.format(user))
print(r.content)