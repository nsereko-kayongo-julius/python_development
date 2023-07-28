from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import csv


#scraping the url
bird_names_url = "https://xeno-canto.org/collection/species/all"
bird_names_response = requests.get(bird_names_url)
bird_names_content = bird_names_response.text
soup = BeautifulSoup(bird_names_content, 'html.parser')

# find all birdnames in the url
bird_common_names = soup.find_all(name="span", class_="common-name")
common_names = []
for name in bird_common_names:
    common_names.append(name.getText())
    print(common_names)

url = "https://xeno-canto.org/api/2/recordings?query=sp"
response_API = requests.get(url)
content = response_API.text

data = response_API.text
parse_json = json.loads(data)
species = parse_json['recordings']
bird_species = []
bird_english_name = []
bird_generic_name = []
bird_song_url = []
bird_song_name = []
bird_song = []

# loop through the json Api and get the species, english name, generic name, song url and song name
for item in species:

    if item["group"] == "birds":
        bird_species.append(item["sp"])
        bird_english_name.append(item["en"])
        bird_generic_name.append(item["gen"])
        bird_song_url.append(item["file"])
        bird_song_name.append(item["file-name"])


# print the species, english name, generic name, song url and song name  in list formart

print(bird_species)
print(bird_generic_name)
print(bird_english_name)
print(bird_song_url)
print(bird_song_name)

# create a csv file and save the species, english name, generic name, song url and song name in the csv file

csv = {
    "bird_species": bird_species,
    "bird_english_name": bird_english_name,
    "bird_generic_name": bird_generic_name,
    "bird_song_url": bird_song_url,
    "bird_song_name": bird_song_name
}
df = pd.DataFrame(csv)
df.to_csv("julius.csv")
print(df.head())

# convert the csv to json file
df.to_json("julius.json")
