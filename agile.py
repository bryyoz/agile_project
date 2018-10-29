
import random
import time

## 
users = [{
    "user_id":1
	"username":"kelvin",
	"email":"kelvin@gmail.com",
	"password":"12345678",
    "role":0
    },
    {
    "user_id":2
    "username":"admin",
	"email":"admin@gmail.com",
	"password":"12345678",
    "role":1
    }] 
comments = []


def login():
    username = input("please input username ")
    password = input("please input password ")

    if not username:
        return 'please input username !!!'
    if not password:
        return 'please input password !!!'


    user = next((item for item in users if item["username"] == username), False)
    if user == False:
        return 'no user with that username exists'
    if user['password'] != password:
        return 'wrong password'




print(login())