#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """
    Récupère les posts depuis l’API et affiche leurs titres.

    Envoie une requête HTTP GET à l’API JSONPlaceholder, vérifie
    le code de réponse et affiche le titre de chaque post si la
    requête est réussie.

    Retour:
        Aucun
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        print("Successful!")
        data = response.json()
        for post in data:
            print(post["title"])
    else:
        print("request fail", response.status_code)


def fetch_and_save_posts():
    """
    Récupère les posts depuis l’API et les enregistre en CSV.

    Télécharge les données JSON depuis l’API JSONPlaceholder,
    extrait les champs id, titre et corps, puis écrit le tout
    dans un fichier 'posts.csv' en UTF-8.

    Retour:
        Aucun
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        print("Successful!")
        data = response.json()
        post_list = []
        for post in data:
            print(post["title"])
            new_post = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            post_list.append(new_post)
    else:
        print("request fail", response.status_code)
        return

    with open("posts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(post_list)
