# Save-Soundcloud v1.0
# SpotifyScrape.py

# Contributor
# Grant Nolasco


import requests
import json
import base64
import operator
import pandas as pd

## URL Navigation

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
URL = 'https://api.spotify.com'

## Client authorization information

# Client ID and Secret are given to developers when they register their app with a website.
# Spotify needs a base64 encoded response so here we format the authorization information.

CLIENT_ID = "e13eaaea650646249d33c0a92d8a2bb0"
CLIENT_SECRET = "463e10b28d724677a7a83e60b742aa59"
temp1 = CLIENT_ID + ":" + CLIENT_SECRET
temp2 = temp1.encode('utf-8','strict')
HEADER_64 = base64.standard_b64encode(temp2)
PARAMS = {'grant_type':'client_credentials'}	# Requested by Spotify for this particular authorization format
AUTH_HEADERS = {'Authorization':b'Basic '+ HEADER_64}    # Provides base64 authorization with requests, also particular for this authorization format

print('Begin Program')

# Workflow for obtaining a token. Could be written into a function.

r = requests.post(TOKEN_URL, data = PARAMS, headers = AUTH_HEADERS)
dictionary = json.loads(r.content)
TOKEN = dictionary['access_token']

# Using token to make API calls

TOKEN_HEADERS = {'Authorization':'Bearer ' + dictionary['access_token']}

playlist_columns = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',
                    'liveness', 'valence', 'tempo', 'title', 'artist']

rap_playlistData = pd.DataFrame(columns = playlist_columns)
country_playlistData = pd.DataFrame(columns = playlist_columns)
metal_playlistData = pd.DataFrame(columns = playlist_columns)

"""
# ===  Acquiring a random song and its features (GENRE: RAP) ===

# Requesting songs from Spotify search API
for i in range(200):
    rap_search = requests.get('https://api.spotify.com/v1/search?q=genre:rap&type=track&limit=50&offset={}'.format(i), headers = TOKEN_HEADERS).json()
    print(i)

    for song in rap_search['tracks']['items']:

        # Extracting song artist
        song_artist = song['artists'][0]['name']

        # Extracting the song title
        song_title = song['name']

        # Extracting the song ID to get the audio features
        song_id = song['id']

        # Extracting the audio features/title of the song ID and appending it to the playlist dataframe
        audio_features = list(requests.get('https://api.spotify.com/v1/audio-features/{}'.format(song_id), headers = TOKEN_HEADERS).json().values())
        song_row = audio_features[:11]
        song_row.append(song_title)
        song_row.append(song_artist)

        # Adding row list to our dataset
        rap_playlistData = rap_playlistData.append(pd.DataFrame([song_row], columns = playlist_columns))

# Converting dataframe into a csv file
rap_playlistData.to_csv('/Users/gnolasco/Desktop/Python_Projects/rap.csv', encoding='utf-8', index=False)\

# ===  Acquiring a random song and its features (GENRE: COUNTRY) ===

# Requesting songs from Spotify search API
for i in range(200):
    country_search = requests.get('https://api.spotify.com/v1/search?q=genre:country&type=track&limit=50&offset={}'.format(i), headers = TOKEN_HEADERS).json()
    print(i)

    for song in country_search['tracks']['items']:

        # Extracting song artist
        song_artist = song['artists'][0]['name']

        # Extracting the song title
        song_title = song['name']

        # Extracting the song ID to get the audio features
        song_id = song['id']

        # Extracting the audio features/title of the song ID and appending it to the playlist dataframe
        audio_features = list(requests.get('https://api.spotify.com/v1/audio-features/{}'.format(song_id), headers = TOKEN_HEADERS).json().values())
        song_row = audio_features[:11]
        song_row.append(song_title)
        song_row.append(song_artist)

        # Adding row list to our dataset
        country_playlistData = country_playlistData.append(pd.DataFrame([song_row], columns = playlist_columns))

# Converting dataframe into a csv file
country_playlistData.to_csv('/Users/gnolasco/Desktop/Python_Projects/country.csv', encoding='utf-8', index=False)

"""
# ===  Acquiring a random song and its features (GENRE: METAL) ===

# Requesting songs from Spotify search API
for i in range(200):
    metal_search = requests.get('https://api.spotify.com/v1/search?q=genre:metal&type=track&limit=50&offset={}'.format(i), headers = TOKEN_HEADERS).json()
    print(i)

    for song in metal_search['tracks']['items']:

        # Extracting song artist
        song_artist = song['artists'][0]['name']

        # Extracting the song title
        song_title = song['name']

        # Extracting the song ID to get the audio features
        song_id = song['id']

        # Extracting the audio features/title of the song ID and appending it to the playlist dataframe
        audio_features = list(requests.get('https://api.spotify.com/v1/audio-features/{}'.format(song_id), headers = TOKEN_HEADERS).json().values())
        song_row = audio_features[:11]
        song_row.append(song_title)
        song_row.append(song_artist)

        # Adding row list to our dataset
        metal_playlistData = metal_playlistData.append(pd.DataFrame([song_row], columns = playlist_columns))

# Converting dataframe into a csv file
metal_playlistData.to_csv('/Users/gnolasco/Desktop/Python_Projects/metal.csv', encoding='utf-8', index=False)

print('\n End Program')
