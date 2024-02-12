import json
from datetime import datetime

filepath = 'templates/commits.json'

with open(filepath, 'r') as file:
    data = json.load(file)


commit_date = data['commit']['author']['date']


date_object = datetime.strptime(commit_date, '%Y-%m-%dT%H:%M:%SZ')

minutes = date_object.minute

print(f'Les minutes extraites de la date du commit sont : {minutes}')
