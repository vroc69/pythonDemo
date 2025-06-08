import json
import os

def load_json(file_name):
    base_path = os.path.join(os.getcwd(), 'data')
    file_path = os.path.join(base_path, file_name)
    with open(file_path, 'r') as file:
        return json.load(file)