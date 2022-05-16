import requests
import json
from time import time

url_users = "https://jsonplaceholder.typicode.com/users"
url_posts = "https://jsonplaceholder.typicode.com/posts"
url_comments = "https://jsonplaceholder.typicode.com/comments"
name = input("Введите имя: ")
t1 = time()
em = []

def all_email():
    param_request = {'key1': 'value1', 'key2': 'value2'}
    users_response = requests.get(url_users, params=param_request)
    posts_response = requests.get(url_posts, params=param_request)
    comments_response = requests.get(url_comments, params=param_request)
    users_res = users_response.json()
    posts_res = posts_response.json()
    com_res = comments_response.json()
    for i in range(len(users_res)):
        if name == (users_res[i]["username"]):
            id = (users_res[i]["id"])
        for j in range(len(posts_res)):
            if id == posts_res[j]["userId"]:
                commid = posts_res[j]["id"]
            for k in range(len(com_res)):
                if commid == com_res[k]["postId"]:
                    print(com_res[k]["email"])

all_email()
t2 = time()
print(t2-t1)