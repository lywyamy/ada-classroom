import requests
import time

path = "https://us1.locationiq.com/v1/search"
LOCATIONIQ_API_KEY = "pk.88bc11497cd865bd41752e2026331bce"
SEVEN_WONDERS = ["Great Wall of China", "Petra", "Colosseum", "Chichen Itza", "Machu Picchu", "Taj Mahal", "Christ the Redeemer"]

### Demo ###
# search_term = "Great Wall of China"
# query_params = {
#     "key": LOCATIONIQ_API_KEY,
#     "q": search_term,
#     "format": "json"
# }

# response = requests.get(path, params=query_params)
# response_body = response.json()

# print(
#     f"The lat and lon of {search_term} is {response_body[0]['lat']}, {response_body[0]['lon']}")
# print(
#     f"The display name of {search_term} is {response_body[0]['display_name']}")
# print(
#     f"{search_term} is a {response_body[0]['type']} {response_body[0]['class']}")

def get_lat_and_lon(location):
    query_params = {
        "key": LOCATIONIQ_API_KEY,
        "q": location,
        "format": "json"
    }

    response = requests.get(path, params=query_params)
    response_body = response.json()
    return response_body[0]['lat'], response_body[0]['lon']

lat_and_lon_info = dict()

for wonder in SEVEN_WONDERS:
    time.sleep(1)
    lat, lon = get_lat_and_lon(wonder)
    info = {"latitude": lat, "longtitude": lon}
    lat_and_lon_info[wonder] = info

for wonder, info in lat_and_lon_info.items():
    print("The latitude and longtitude of {} is {} and {}.".format(wonder, info["latitude"], info["longtitude"]))