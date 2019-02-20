# client access token: BLLu9NoIW0OIVHhbL5Sfy71H4UL6jIIz-LU1LxGtxunB5k_-4Oz9DGiZcbl5T_7g
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import nltk

# receive song and artist name and send request to Genius API
def request_song_info(song_title, artist_name):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + 'BLLu9NoIW0OIVHhbL5Sfy71H4UL6jIIz-LU1LxGtxunB5k_-4Oz9DGiZcbl5T_7g'}
    search_url = base_url + '/search'
    data = {'q': song_title + ' ' + artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    # response contains information about all matches found in the API
    return response

# receive song url and use BeautifulSoup to pull data from HTML file
def scrape_song_url(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find('div', class_='lyrics').get_text()
    return lyrics

# read in rap song titles and artist names from CSV file
rap_df = pd.read_csv('/Users/gnolasco/Desktop/Python_Projects/SpotifyPrediction/rap_january.csv',sep=',')
rapsongs = list(rap_df['title'])
rapartists = list(rap_df['artist'])
raplyrics = list()

# read in country song titles and artist names from CSV file
country_df = pd.read_csv('/Users/gnolasco/Desktop/Python_Projects/SpotifyPrediction/country_january.csv',sep=',')
countrysongs = list(country_df['title'])
countryartists = list(country_df['artist'])
countrylyrics = list()

# read in metal song titles and artist names from CSV file
metal_df = pd.read_csv('/Users/gnolasco/Desktop/Python_Projects/SpotifyPrediction/metal_january.csv',sep=',')
metalsongs = list(metal_df['title'])
metalartists = list(metal_df['artist'])
metallyrics = list()

# === RAP ===
# iterate through rap songs and artist names to scrape lyrics
try:
    for i in range(4402+1,len(rapsongs)):
        print(i)
        song = rapsongs[i]
        artist = rapartists[i]
        # collect song info in response
        response = request_song_info(song, artist)
        # convert to json
        json = response.json()
        remote_song_info = None
        # iterate through matches
        for hit in json['response']['hits']:
            if artist.lower() in hit['result']['primary_artist']['name'].lower():
                # define remote_song_info if Genius API has information on song
                remote_song_info = hit
                break
        if remote_song_info:
            # take song url from remote_song_info, scrape lyrics from url
            song_url = remote_song_info['result']['url']
            lyr=scrape_song_url(song_url)
        else:
            # output 'Not Found' if Genius API does not have song info
            lyr='Not Found'
        # append lyrics to list
        raplyrics.append(lyr)

    with open('rap_lyricsV3.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(raplyrics)

    csvFile.close()
except:
    with open('rap_lyricsV3.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(raplyrics)

    csvFile.close()

"""
# === COUNTRY ===

# iterate through country songs and artist names to scrape lyrics
try:
    for i in range(633+1, len(countrysongs)):
        print(i)
        song = countrysongs[i]
        artist = countryartists[i]
        # collect song info in response
        response = request_song_info(song, artist)
        # convert to json
        json = response.json()
        remote_song_info = None
        # iterate through matches
        for hit in json['response']['hits']:
            if artist.lower() in hit['result']['primary_artist']['name'].lower():
                # define remote_song_info if Genius API has information on song
                remote_song_info = hit
                break
        if remote_song_info:
            # take song url from remote_song_info, scrape lyrics from url
            song_url = remote_song_info['result']['url']
            lyr=scrape_song_url(song_url)
        else:
            # output 'Not Found' if Genius API does not have song info
            lyr='Not Found'
        # append lyrics to list
        countrylyrics.append(lyr)

    with open('country_lyricsV3.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(countrylyrics)

    csvFile.close()
except:
    with open('country_lyricsV3.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(countrylyrics)

    csvFile.close()

# === METAL ===

# iterate through metal songs and artist names to scrape lyrics
try:
    for i in range(len(metalsongs)):
        print(i)
        song = metalsongs[i]
        artist = metalartists[i]
        # collect song info in response
        response = request_song_info(song, artist)
        # convert to json
        json = response.json()
        remote_song_info = None
        # iterate through matches
        for hit in json['response']['hits']:
            if artist.lower() in hit['result']['primary_artist']['name'].lower():
                # define remote_song_info if Genius API has information on song
                remote_song_info = hit
                break
        if remote_song_info:
            # take song url from remote_song_info, scrape lyrics from url
            song_url = remote_song_info['result']['url']
            lyr=scrape_song_url(song_url)
        else:
            # output 'Not Found' if Genius API does not have song info
            lyr='Not Found'
        # append lyrics to list
        metallyrics.append(lyr)

    with open('metal_lyricsV1.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(metallyrics)

    csvFile.close()
except:
    with open('metal_lyricsV1.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(metallyrics)

    csvFile.close()

# combine rap songs, artists, lyrics into dataframe
#rap_df['Lyrics'] = pd.Series(raplyrics)

#rap_df.to_csv('/Users/gnolasco/Desktop/Python_Projects/SpotifyPrediction/rap_withLyrics.csv', encoding='utf-8', index=False)
"""
