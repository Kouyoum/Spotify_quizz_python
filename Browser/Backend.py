
import spotipy, requests, json, time, pandas as pd
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import random as random
import time as time
import authorization as aut


sp, token = aut.authorization()

"""
-----DATABASE BUILDER-----
This function builds the database with successive API calls
The following tables are created.
For detailed information, refer to the DB guide (schema, primary key)
"""

#PERSONAL DATA
"""This function enables to record the user's spotify idea"""
def find_username_user():
    result = sp.me()
    username = result['id']
    return username

username = find_username_user()
#print(username)

#USER TOP PLAYED TRACKS
# function returning dataframe
def user_top_tracks():
    timespan = 'long_term'  #short = 4 weeks, medium = 6 months, long = several years
    limit = 50              #Max 50
    result = sp.current_user_top_tracks(limit, time_range= timespan)

    track_name = []
    artist = []
    artist_id = []
    popularity = []
    explicit = []
    track_id = []
    album_name = []
    album_year = []
    uri = []

    #iterate through API result
    for item in result['items']:
        track_name.append(item['name'])
        popularity.append(item['popularity'])
        explicit.append(item['explicit'])
        track_id.append(item['id'])
        uri.append(item['uri'])
        album_name.append(item['album']['name'])
        album_year.append(item['album']['release_date'][0:4])
        for art in item['artists']:
            artist.append(art['name'])
            artist_id.append(art['id'])
            break

    # print('')
    # print('WE RETREIVED DATA FOR YOUR TOP  ' ,len(track_name), ' TRACKS')
    # print('')
    # print('')

    #create dataframe
    toptrack = pd.DataFrame()
    toptrack['Track ID'] = track_id
    toptrack['Track'] = track_name
    toptrack['Artist'] = artist
    toptrack['Artist ID'] = artist_id
    toptrack['Popularity'] = popularity
    toptrack['Explicit'] = explicit
    toptrack['Album Name'] = album_name
    toptrack['Album Year'] = album_year
    toptrack['URI'] = uri

    return toptrack

""" EXECUTE THE FUNCTION TO OBTAIN THE 50 TRACKS & INFORMATION"""
toptrack = user_top_tracks()
#print(toptrack)


#USER TOP PLAYED ARTISTS
# Function returning dataframe of user's top artists
def topartist():
    timespan = 'long_term'  #short = 4 weeks, medium = 6 months, long = several years
    limit = 50              #Max 50
    result = sp.current_user_top_artists(limit, time_range=timespan)

    top_artist = []
    popularity = []
    artist_id = []

    for item in result['items']:
        top_artist.append(item['name'])
        popularity.append(item['popularity'])
        artist_id.append(item['id'])

    topartist = pd.DataFrame()
    topartist['Top Artist'] = top_artist
    topartist['Popularity'] = popularity
    topartist['Artist ID'] = artist_id
    #topartist.to_csv('top_artist.csv',index=False)
    return topartist

""" EXECUTE THE FUNCTION TO OBTAIN THE 50 ARTISTS & INFORMATION"""
topartist = topartist()
#print(topartist)

# #USER PLAYLIST
""" THIS FUNCTION RETURNS A DATAFRAME OF ALL THE USER'S PLAYLISTS"""
def playlist():
	result = sp.current_user_playlists()

	playlist_id = []
	name = []
	public = []
	collaborative = []
	tracks = []
	is_yours = []

	for item in result['items']:
	    playlist_id.append(item['id'])
	    name.append(item['name'])
	    public.append(item['public'])
	    collaborative.append(item['collaborative'])
	    tracks.append(item['tracks']['total'])
	    if item['owner']['id'] == username:
	        is_yours.append(1)
	    else:
	        is_yours.append(0)

	playlists = pd.DataFrame()
	playlists['Playlist ID'] = playlist_id
	playlists['Name'] = name
	playlists['Public'] = public
	playlists['Collaborative'] = collaborative
	playlists['Tracks'] = tracks
	playlists["Is Yours"] = is_yours
	return playlists

# playlists.to_csv('playlists.csv',index=False)
#playlists = playlist()
#print(playlists)

#
""" THIS FUNCTION CREATES A CSV FILE OF THE USER's TOP ARTIST"""
def export_csv():
	print("DO YOU WANT TO EXPORT YOUR TOP 50 TRACKS AND TOP 50 ARTISTS TO A CSV TABLE ?")
	print("y/n ?")
	u_input = input()
	if u_input == "y":
		toptrack.to_csv('top_track.csv',index=False)
		print('SUCCESFULLY EXPORTED top_track.csv')
		topartist.to_csv('top_artist.csv',index=False)
		print('SUCCESFULLY EXPORTED top_artist.csv')
		return
	return

"""
# # ----- API CALLS -----
# # This section contains functions to retrieve data from spotify.
# # """
# #
def tracks(track_id):
	result = sp.tracks(track_id)

	track_name = []
	track_id = []

	for item in result['tracks']:
	    track_name.append(item['name'])
	    track_id.append(item['id'])

	track = pd.DataFrame()
	track['Track Name'] = track_name
	track['Track ID'] = track_id
	return track

""" THIS FUNCTION RETURNS THE CHARACTERISTICS (LIKE ACOUSTIC) OF A SONG"""
def audio_features(song_id):
	result = sp.audio_features(song_id)

	track_id = []
	acousticness = []
	danceability = []
	loudness = []
	liveness = []
	instrumentalness = []
	speechiness = []

	for item in result:
	    track_id.append(item['id'])
	    acousticness.append(item['acousticness'])
	    danceability.append(item['danceability'])
	    loudness.append(item['loudness'])
	    liveness.append(item['liveness'])
	    instrumentalness.append(item['instrumentalness'])
	    speechiness.append(item['speechiness'])

	song_characteristic = pd.DataFrame()
	song_characteristic['Track ID'] = track_id
	song_characteristic['Acousticness'] = acousticness
	song_characteristic['Danceability'] = danceability
	song_characteristic['Loudness'] = loudness
	song_characteristic['Liveness'] = liveness
	song_characteristic['Instrumentalness'] = instrumentalness
	song_characteristic['Speechiness'] = speechiness

	return song_characteristic


""" THIS FUNCTION RETURNS A DataFrame WITH ARTIST INFO, AMONGST OTHERS, AN ARTIST'S GENRES """
""" Args: Function takes a dataframe, called artists, as argument.
    artists correspond to potential artists to the question. """
def artist_api(artists):
	result = sp.artists(artists)
	artist_id = []
	name = []
	followers = []
	popularity = []
	genres = []

	for item in result['artists']:
	    artist_id.append(item['id'])
	    name.append(item['name'])
	    followers.append(item['followers']['total'])
	    popularity.append(item['popularity'])
	    genres.append(item['genres'])

	artists = pd.DataFrame()
	artists['Artist ID'] = artist_id
	artists['Name'] = name
	artists['Followers'] = followers
	artists['Popularity'] = popularity
	artists['Genres'] = genres
	return artists

""" THIS FUNCTION CREATES A PLAYLIST OF THE USER's 50 MOST HEARD TRACKS"""
def create_playlist():
	# This funtion is used to create a playlist containing the top 50 tracks of the user.
	print("DO YOU WANT TO CREATE A PLAYLIST OF YOUR TOP 50 TRACKS ?")
	print("y/n ?")
	#u_input = input()
	#if u_input == "y":
	sp.user_playlist_create(username, name='TOP 50 TRACKS', public=True, description='This playlist was created thanks to a Python Project')
	sp.user_playlist_add_tracks(username, playlist_id=playlist()['Playlist ID'][0], tracks=toptrack['Track ID'], position=None)

	return

"""
----- PLAYBACK -----
This is used to play / pause tracks on your current device during the quizz
"""
# def playback10s(track_uri):
# 	# This function is used to play the first 10 secondes of the correct answer of the questions of the quiz
# 	devices = sp.devices()
# 	for i in devices['devices']:
# 		device_id = i['id']
# 		break
# 	sp.start_playback(device_id=device_id  ,uris=track_uri)
# 	print('...PLAYING SONG FOR 10 SECONDES ON DEVICE')
# 	time.sleep(10)
# 	sp.pause_playback()

def playback10s():
	# This function is used to play the first 10 secondes of the correct answer of the questions of the quiz
    devices = sp.devices()
    dic_device = devices['devices'][0]
    id = dic_device['id']
    return id

# device = playback10s()
# dic_device = device['devices'][0]
# id = device1['id']
# print(id)


# Things to EXECUTE
# if __name__ == "__main__":
#     print("Backend imported")
