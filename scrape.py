from dotenv import load_dotenv
import os
import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=2)
    print(text)

load_dotenv()
KEY = os.getenv("MUSIXMATCH_API_KEY")
url = "https://api.musixmatch.com/ws/1.1/"

params = {
	"apikey" : KEY,
	"q_artist" : "Arctic Monkeys",
	"page_size": 1
}

# PROD
# a = requests.get(url + "artist.search",params=params).json()
# END PROD

# TEST
a = json.load(open("json/output1.json","r"))
# END TEST

# jprint(a)
artist_id = a["message"]["body"]["artist_list"][0]["artist"]["artist_id"]

params = {
	"apikey" : KEY,
	"artist_id" : artist_id
}

# PROD
# b = requests.get(url + "artist.albums.get",params=params).json()
# END PROD

# TEST
b = json.load(open("json/output2.json","r"))
# END TEST

album_list = b["message"]["body"]["album_list"]

album_id_list = []

for album in album_list:
	album_id_list.append(album["album"]["album_id"])

# print(album_id_list)

c = []

# PROD
# for album_id in album_id_list:
# 	params = {
# 		"apikey" : KEY,
# 		"album_id" : album_id
# 	}
# 	c.append(requests.get(url + "album.tracks.get",params=params).json())



# for i in range(0,len(c)):
# 	f = open(f"json/output{3+i}.json","w")
# 	f.write(json.dumps(c[i], sort_keys=True, indent=2))
# END PROD

# TEST
for i in range(3,13):
	c.append(json.load(open(f"json/output{i}.json","r")))
# END TEST

track_id_list = []
track_names = []

for i in c:
	for j in i["message"]["body"]["track_list"]:
		track_id_list.append(j["track"]["track_id"])
		track_names.append(j["track"]["track_name"])

print(track_names)


