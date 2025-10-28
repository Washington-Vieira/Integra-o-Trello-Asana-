import requests
from config import ASANA_TOKEN

BASE_URL = "https://app.asana.com/api/1.0/"
HEADERS = {"Authorization": f"Bearer {ASANA_TOKEN}", "Content-Type": "application/json"}

def get_workspaces():
    url = BASE_URL + "workspaces"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()['data']

def create_project(name, workspace):
    url = BASE_URL + "projects"
    data = {"data": {"name": name, "workspace": workspace}}
    response = requests.post(url, json=data, headers=HEADERS)
    response.raise_for_status()
    return response.json()['data']['gid']

def create_section(project_id, name):
    url = BASE_URL + f"projects/{project_id}/sections"
    data = {"data": {"name": name}}
    response = requests.post(url, json=data, headers=HEADERS)
    response.raise_for_status()
    return response.json()['data']['gid']

def create_task(name, notes, project_id, section_id):
    url = BASE_URL + "tasks"
    data = {
        "data": {
            "name": name,
            "notes": notes,
            "projects": [project_id],
            "memberships": [{"project": project_id, "section": section_id}]
        }
    }
    response = requests.post(url, json=data, headers=HEADERS)
    response.raise_for_status()
    return response.json()
