import os
import json 


#Create data that you can work with

def load_json():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "office_list.json")
    
    offices = None
    with open(json_url) as f:
        offices = json.loads(f.read())
    if offices is None:
        return []
    return offices

def save_json(offices):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "office_list.json")
    with open(json_url,'w') as f:
        f.write(json.dumps(offices))

def get_offices():
    offices = load_json()
    return offices

def add_office(office):
    offices = load_json()
    offices.append(office)
    save_json(offices)

def get_office(id):
    offices = load_json()
    found_office = None

    for office in offices:
        if office['id'] == id:
            found_office = office

    return found_office


    


