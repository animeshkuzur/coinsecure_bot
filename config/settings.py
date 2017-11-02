import json
from os.path import join, dirname

json_path = join(dirname(__file__), 'config.json')
with open(json_path) as json_data:
    data = json.load(json_data)

API_KEY = data['app']['key']

APP_DEBUG = data['app']['debug']

BASE_URL = data['app']['base_url']
