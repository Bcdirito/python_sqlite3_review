import requests
import random
import json

met_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

initial_get_request = requests.get(met_url)
get_request_content = ""
object_keys = []

if initial_get_request.status_code == 200:
    get_request_content = json.loads(initial_get_request.content)
    for key in get_request_content.keys():
        object_keys.append(key)
    print(f"Request Successful")
else:
    print("Request Failed")

object_ids = object_keys[-1]

def get_random_tour_ids(content, ids_key):
    random.shuffle(content[ids_key])
    return content[ids_key][0:10]

def get_random_tour_content(ids):
    art_objects_list = []
    for obj in ids:
        response = requests.get(f"{met_url}/{obj}")
        if response.status_code == 200:
            art_objects_list.append(json.loads(response.content))
            
    return art_objects_list

def get_tour_content_titles_and_artists(objects_list):
    for obj in objects_list:
        print(f"{obj['title']} - {obj['artistDisplayName']}")
        
print(get_tour_content_titles_and_artists(get_random_tour_content(get_random_tour_ids(get_request_content, object_ids))))
    