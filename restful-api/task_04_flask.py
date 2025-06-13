#!/usr/bin/python3
"""
Flask API for user management.

This module provides a simple REST API using Flask to manage users.
It includes endpoints for retrieving user data, adding new users,
and checking API status.
"""

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """
    Home endpoint.

    Returns:
        str: Welcome message for the Flask API.
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """
    Get all usernames.

    Returns:
        json: List of all usernames stored in the API.
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    API status endpoint.

    Returns:
        str: Status of the API (always "OK").
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Get user details by username.

    Args:
        username (str): The username to retrieve.
    Returns:
        json: User data if found, error message if not found.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user to the API.

    Expects JSON data with at least a 'username' field.
    *
    Returns:
        json: Success message with user data (201) or error message (400).
    """
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
