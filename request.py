import requests


BASE_URL = "http://127.0.0.1:8000/account/student-count/"

h = {
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyOTg5MDk0MSwiaWF0IjoxNzI5Mjg2MTQxLCJqdGkiOiJkMzM3Njg5MGJlOTY0YWZkYTg5YWM2MjNmNDdlNjdkOCIsInVzZXJfaWQiOjE0fQ.bSJjfc9jIVfe-3XHsWvCVN2jE77P_s1Y2oaduQljwnw","access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwNDk1NzQxLCJpYXQiOjE3MjkyODYxNDEsImp0aSI6IjkyYmU3NTE4ODFkZTRkOWI4MTM3ZjMxZjI1ZWFhYzUxIiwidXNlcl9pZCI6MTR9.fdErzqREb2zG0CoRVB0esXJVW6HHFc-U7fHlmc7l8JE"
}
r = requests.get(BASE_URL, headers=h)

print(r.status_code)
print(r.headers)
print(r.text)