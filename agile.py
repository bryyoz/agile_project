
import random
import datetime

## Data stores for users and comments
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

# loggs in the user
def login():
    username = input("please input username ")
    password = input("please input password ")

    if not username:
        return 'please input username !!!'
    if not password:
        return 'please input password !!!'

# check if username exists
    user = next((item for item in users if item["username"] == username), False)

# if username by the given name  doesnt exist 
    if user == False:
        return 'no user with that username exists'


    if user['password'] != password:
        return 'wrong password'
    user["lastLoginAt"] = datetime.datetime.now()

    if user['role']== 0:
        normal_user = input("1. create comment \n 2.edit comment \n  3. logout ")
        if normal_user == str("1"):
            user_id = input("Enter your user id:")
            if not user_id:
                return 'You must enter a user_id' 
            comment = input("Type your comment here:")
            if not comment:
                return 'You must enter a comment'
            data = {'comment_id': len(comments) +1,
            'comment': comment,
            'timestamp': datetime.datetime.now() ,
            'created_by': user_id
            }
            comments.append(data)
            return comments
        if normal_user == str("2"):
            comment_id = int(input("Enter the comment id:"))
            
            if not comment_id:
                return 'You must enter the comment id'
            comm = next((comment for comment in comments if comment["comment_id"] == comment_id), False)
            if comm == False:
                return 'Comment not found!'
            new_comment = input("Enter your comment here:")
            comm["comment"] = new_comment
            return comments
        if normal_user == str("3"):
            login()

    if user['role']== 1:
        moderator_user = input("1. create comment \n 2. edit comment \n 3. delete comment \n 4. logout \n ")
        if moderator_user == str("1"):
            user_id = input("Enter your user id:")
            if not user_id:
                return 'You must enter a user_id' 
            comment = input("Type your comment here:")
            if not comment:
                return 'You must enter a comment'
            data = {'comment_id': len(comments) +1,
            'comment': comment,
            'timestamp': datetime.datetime.now() ,
            'created_by': user_id
            }
            comments.append(data)
            return comments
        if moderator_user == str("2"):
            comment_id = int(input("Enter the comment id:"))
            
            if not comment_id:
                return 'You must enter the comment id'
            comm = next((comment for comment in comments if comment["comment_id"] == comment_id), False)
            if comm == False:
                return 'Comment not found!'
            new_comment = input("Enter your comment here:")
            comm["comment"] = new_comment
            return comments
        if moderator_user == str("3"):
            comment_id = int(input("Enter the comment id to delete:")) 
            if not comment_id:
                return 'You must enter the comment id'
            comm = next((comment for comment in comments if comment["comment_id"] == comment_id), False)

            if comm == False:
                return 'Comment not found!'
            comments.remove(comm)
            return comments
        if moderator_user == str("4"):
            login()
    
    if user['role']== 2:
        admin_user = input("1. create comment \n  2.edit comment \n 3. delete comment \n 4. logout \n ")
        if admin_user == str("1"):
            user_id = input("Enter your user id:")
            if not user_id:
                return 'You must enter a user_id' 
            comment = input("Type your comment here:")
            if not comment:
                return 'You must enter a comment'
            data = {'comment_id': len(comments) +1,
            'comment': comment,
            'timestamp': datetime.datetime.now() ,
            'created_by': user_id
            }
            comments.append(data)
            return comments
        if admin_user == str("2"):
            comment_id = int(input("Enter the comment id:"))
            
            if not comment_id:
                return 'You must enter the comment id'
            comm = next((comment for comment in comments if comment["comment_id"] == comment_id), False)
            if comm == False:
                return 'Comment not found!'
            new_comment = input("Enter your comment here:")
            comm["comment"] = new_comment
            return comments
        if admin_user == str("3"):
            comment_id = int(input("Enter the comment id to delete:")) 
            if not comment_id:
                return 'You must enter the comment id'
            comm = next((comment for comment in comments if comment["comment_id"] == comment_id), False)

            if comm == False:
                return 'Comment not found!'
            comments.remove(comm)
            return comments

        if admin_user == str("4"):
            login()  




print(login())