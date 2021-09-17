import requests
import json


response = requests.get("https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json")
postcode_map = response.content
postcode_map = json.loads(postcode_map)
postinumero = input("Kirjoita postinumero: ")
print(postcode_map[postinumero])