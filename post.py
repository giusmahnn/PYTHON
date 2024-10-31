import requests

BASE_URL = "http://127.0.0.1:8000/account/login/"

# first_name = input("First Name: ")
# last_name = input("Last Name: ")
email = input("Email: ")
password = input("Password: ")

data = {}
# data["first_name"] = first_name
# data["last_name"] = last_name
data["email"] = email
data["password"] = password

h = {
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyOTg5MDk0MSwiaWF0IjoxNzI5Mjg2MTQxLCJqdGkiOiJkMzM3Njg5MGJlOTY0YWZkYTg5YWM2MjNmNDdlNjdkOCIsInVzZXJfaWQiOjE0fQ.bSJjfc9jIVfe-3XHsWvCVN2jE77P_s1Y2oaduQljwnw","access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwNDk1NzQxLCJpYXQiOjE3MjkyODYxNDEsImp0aSI6IjkyYmU3NTE4ODFkZTRkOWI4MTM3ZjMxZjI1ZWFhYzUxIiwidXNlcl9pZCI6MTR9.fdErzqREb2zG0CoRVB0esXJVW6HHFc-U7fHlmc7l8JE"
}

r = requests.post(BASE_URL, data=data, headers=h)

print(r.status_code)
print(r.headers["Content-Type"])
print(r.headers)
print(r.text)
try:
    print(r.content)
except:
    print("Error")