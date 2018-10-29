
import random
import datetime

## 
users = [{
    "user_id":1,
	"username":"kelvin",
	"email":"kelvin@gmail.com",
	"password":"12345678",
    "role":0,
    "lastLoginAt": ""
    },
    {
    "user_id":2,
    "username":"admin",
	"email":"admin@gmail.com",
	"password":"12345678",
    "role":1,
    "lastLoginAt": ""
    },
        {
    "user_id":3,
    "username":"superadmin",
	"email":"superadmin@gmail.com",
	"password":"12345678",
    "role":2,
    "lastLoginAt": ""
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
    user["lastLoginAt"] = datetime.datetime.now()

    if user['role']== 0:
        normal_user = input("1. create comment /n 2.edit comment /")

    if user['role']== 1:
        moderator_user = input("1. create comment /n  2.edit comment /n 3.delete comment")
    
    if user['role']== 2:
        admin_user = input("1. create comment /n  2.edit comment /n 3.delete comment")




print(login())