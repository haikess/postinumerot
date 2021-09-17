import requests
import json


def fix_smartpost_typos(postcode_map):
    # smart post ja smartpsot korjataan olemaan smartpost:
    for name in postcode_map:
        if "SMART POST" == postcode_map[name]:
            postcode_map[name] = "SMARTPOST"
        if postcode_map[name] == "SMARTPSOT":
            postcode_map[name] = "SMARTPOST"
    return postcode_map


def get_postcode_map():
    response = requests.get("https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json")
    postcode_map = response.content
    postcode_map = json.loads(postcode_map)
    # alempi rivi korjaa bugin. Bugi ilmenee jos kyseinen rivi kommentoidaan pois
    postcode_map = fix_smartpost_typos(postcode_map)
    return postcode_map


def get_postcode_by_municipality(postitoimipaikka, postcode_map):
    postinumerot = []
    for postcode in postcode_map:
        # replace korjaa kaikista välilyönnin:
        if postcode_map[postcode].replace(" ", "") == postitoimipaikka:
            # print(postcode)
            postinumerot.append(postcode)
    return postinumerot


if __name__ == "__main__":
    postcode_map = get_postcode_map()
    postitoimipaikka = input("Kirjoita postitoimipaikka: ").upper()
    postinumerot = get_postcode_by_municipality(postitoimipaikka, postcode_map)
    print("Postinumerot: " + ", ".join(postinumerot))

