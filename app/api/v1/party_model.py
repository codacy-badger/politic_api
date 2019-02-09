import os
import json 


#Create data that you can work with

def load_json():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "party_list.json")
    
    parties = None
    with open(json_url) as f:
        parties = json.loads(f.read())
    if parties is None:
        return []
    return parties

def save_json(parties):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "party_list.json")
    with open(json_url,'w') as f:
        f.write(json.dumps(parties))

def get_parties():
    parties = load_json()
    return parties

def add_party(party):
    parties = load_json()
    parties.append(party)
    save_json(parties)

def get_party(id):
    parties = load_json()
    found_party = None

    for party in parties:
        if party['id'] == id:
            found_party = party

    return found_party


    


