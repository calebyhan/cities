import requests
import os

URL = "https://api.teleport.org/api/"


def search(query):
    response = requests.get(URL + f"cities/?search={query}").json()

    i = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Is this your city: " + response["_embedded"]["city:search-results"][i]["matching_full_name"])
        if input("Y/N: ").upper() == "Y":
            break
        i += 1
    return response["_embedded"]["city:search-results"][i]["_links"]["city:item"]["href"]


def city(link):
    response = requests.get(link).json()

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Location: {response['full_name']}")
    print(f"ID: {response['geoname_id']}")
    print(f"Population: {response['population']}")
    print(f"Coordinates: ({response['location']['latlon']['latitude']}, {response['location']['latlon']['longitude']})")


city(search("knoxville"))
