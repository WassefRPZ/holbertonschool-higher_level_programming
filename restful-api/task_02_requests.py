#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        my_list = []
        for post in posts:
            new_dict = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body'],
            }
            my_list.append(new_dict)
        with open ('posts.csv','w', newline='', encoding='utf-8') as csvfil:
            fieldnames = ['id','title', 'body']
            writer = csv.DictWriter(csvfil, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(my_list)