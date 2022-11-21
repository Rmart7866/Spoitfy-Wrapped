import spotipy
import time
import subprocess
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth

#spotipy auhtorization
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="8f706b099b3f45bf98514edaaca88f99",
                                               client_secret="a4cd5b0cdb5c46d8b556a3823fa840d7",
                                               redirect_uri="http://localhost",
                                               scope="user-top-read"))

#this function gets the songs within the selected time frame (past month, past few months, past few years)
def get_track_ids(time_frame):
    track_ids = []
    for song in time_frame['items']:
        track_ids.append(song['id'])
    return track_ids
#this fucntion gets the information from the track ID
def get_track_features(id):
    meta = sp.track(id)
    # meta
    name = meta["name"]
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    spotify_url = meta['external_urls']['spotify']
    album_cover = meta['album']['images'][0]['url']
    track_info = [name, album, artist]
    return track_info
# loop over track ids
#this function converts the tracks into an organized data frame
def convert_to_df(track_ids, time_period):
    # loop over track ids
    tracks = []
    for i in range(len(track_ids)):
        time.sleep(.5)
        track = get_track_features(track_ids[i])
        tracks.append(track)
    # create dataset
    df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist'])
    # save to CSV
    #df.to_csv(f'{today}-{time_period}.csv')

    #seperates the groups of songs inot their repsective files 
    if time_period == 'short_term':
        df.to_csv("test.csv",sep="^")
    if time_period == 'medium_term':
        df.to_csv("test2.csv",sep="^")
    if time_period == 'long_term':
        df.to_csv("test3.csv",sep="^")

#main fucntion
answer = input("Do you want to check out your Spotify wrapped?(Y/N) ")
if (answer == 'Y' or answer == 'y'):
    time_ranges = ['medium_term', 'long_term', 'short_term']
    for time_period in time_ranges:
        top_tracks = sp.current_user_top_tracks(limit=20, offset=0, time_range=time_period)
        track_ids = get_track_ids(top_tracks) 
        convert_to_df(track_ids, time_period)
    #calls php file, which updates it with the correct selection of tracks     
    subprocess.call('php ./webpage.php', stdin=None, stdout=None, stderr=None, shell=True)
    print("Enter this link in your browser!")
    #link to the website 
    print("https://rmarti20.w3.uvm.edu/M3EOP-Rmarti20/webpage.php")
else:
    print ("ok bye")
