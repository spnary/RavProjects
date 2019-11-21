import os
import requests
import base64
import json

rav_username = os.getenv('RAV_USERNAME')
rav_password = os.getenv('RAV_PASSWORD')

class RavelryProject:
    def __init__(self, dict):
        self.name = dict['name']
        self.pattern = dict['pattern_name']


    def __str__(self):
        name = self.name if self.name != None else "None"
        pattern = self.pattern if self.pattern != None else  "None"
        return name + " / " + pattern

    
def projectRequest(username, password):
    header_string = username + ':' + password
    auth_header_bytes = base64.urlsafe_b64encode(header_string.encode('utf-8'))
    auth_header = str(auth_header_bytes, 'utf-8')

    headers = {
        'Authorization': 'Basic ' + auth_header
    }
    url = 'https://api.ravelry.com/projects/spnary/list.json'

    r = requests.get(url, headers=headers)
    return r.json()


def writeProjectsToFile(projects, filename):
    pretty_data = json.dumps(projects, indent=4)
    project_list = open(filename, 'w')
    project_list.write(pretty_data)
    project_list.close()


data = projectRequest(rav_username, rav_password)
writeProjectsToFile(data, 'projects-list.json')
projects_array = data['projects']

projects = []

for project in projects_array:
    rav_project = RavelryProject(project)
    projects.append(rav_project)

for project in projects:
    print(project)
