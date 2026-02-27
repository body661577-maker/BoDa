import requests
import os

class ConfigLoader:
    def __init__(self, config_url):
        self.config_url = config_url
        self.config = self.load_config()

    def load_config(self):
        response = requests.get(self.config_url)
        response.raise_for_status()
        return response.json()

    def get(self, key):
        return self.config.get(key)

class LoginLogoutNotifier:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_event(self, message):
        data = {'content': message}
        requests.post(self.webhook_url, json=data)

# Example usage:
# config_loader = ConfigLoader('https://raw.githubusercontent.com/user/repo/branch/config.json')
# notifier = LoginLogoutNotifier('https://discord.com/api/webhooks/your_webhook_url')
# notifier.send_event('User logged in')
