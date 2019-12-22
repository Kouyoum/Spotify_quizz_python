
import spotipy
import requests
import json
import time
import pandas as pd
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

# PERSONAL DATA


def find_username_user():
    """  RECORD USER ID

    Returns:

    username: user's spotify user id """
    result = sp.me()
    username = result['id']
    return username


username = find_username_user()

# print(username)

# USER TOP PLAYED TRACKS
# function returning dataframe


def user_top_tracks():
    """
        USER TOP 50 TRACKS ON SPOTIFY

    Returns:

    toptrack: pandas dataframe of the user's top 50 tracks.

    Includes the following attributes:track id, track name, artist, artist id,
    popularity, explicit, album_name, album_year, uri

    """
    timespan = 'long_term'  # short = 4 weeks, medium = 6 months, long = several years
    limit = 50  # Max 50
    result = sp.current_user_top_tracks(limit, time_range=timespan)

    track_name = []
    artist = []
    artist_id = []
    popularity = []
    explicit = []
    track_id = []
    album_name = []
    album_year = []
    uri = []

    # iterate through API result
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

    # create dataframe
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
# print(toptrack)


def get_genres():
    """ AVAILABLE GENRES ON SPOTIFY

    Returns:

    Genres: Dataframe of the available genres on spotify
    """
    results = sp.recommendation_genre_seeds()
    result = results['genres']
    # # list creation to unpack the json file
    # genres = []
    # for item in result["genres"]:
    #     genres.append(item['genres'])
    Genres = pd.DataFrame()
    Genres['genres categories'] = result
    return Genres


def topartist():
    """ USER TOP PLAYED ARTISTS

    Returns:

    Dataframe of user's most heard artists, and attributes: popularity, name, id """
    timespan = 'long_term'  # short = 4 weeks, medium = 6 months, long = several years
    limit = 50  # Max 50
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
    # topartist.to_csv('top_artist.csv',index=False)
    return topartist


""" EXECUTE THE FUNCTION TO OBTAIN THE 50 ARTISTS & INFORMATION"""
topartist = topartist()


def playlist():
    """ USER PLAYLIST

    Returns:

    Dataframe of all the user's playlists and information.
    """
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


def export_csv():
    """ CSV FILE CREATED OF THE USER's TOP ARTIST"""
    toptrack.to_csv('top_track.csv', index=False)
    topartist.to_csv('top_artist.csv', index=False)
    return "Done"



### API CALLS - THE FUNCTION BELOW QUERY SPOTIFY API DO OBTAIN ADDITIONAL
### INFORMATION ABOUT THE TRACKS, ALBUMS, ARTISTS, ...


def tracks(track_id):
    """FIND TRACK NAME FROM ITS ID

     Args:
     track_id: string variable, id of a spotify track

     Returns:
     track: name of the track corresponding to the id"""
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



def audio_features(song_id):
    """ FIND THE CHARACTERISTICS (LIKE ACOUSTIC) OF A SONG

    Args:

    song_id: id of the track we are interested in

    Return:

    song_characteristic: Pandas dataframe containing information about the track

    such as: danceability, loudness, liveness, ..."""

    # Function from the spotipy package, returning a json
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




def artist_api(artists):
    """ GET ARTIST INFO, GENRES, ...

        Args:

        artists: a list of artist IDs, URIs or URLs

        Returns:

        artists: pandas dataframe of artist(s) with information.
        Attributes include followers, popularity, ...

        """
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
    """ This funtion is used to create a playlist containing the top 50 tracks of the user. """
    sp.user_playlist_create(username, name='TOP 50 TRACKS', public=True)
    sp.user_playlist_add_tracks(username, playlist_id=playlist(
    )['Playlist ID'][0], tracks=toptrack['Track ID'], position=None)

    return "Done"



"""
----- PLAYBACK -----
Those functions were not used in the end, as a an easier solution was found

This is used to play / pause tracks on your current device during the quizz
"""
def playback10s(track_uri):

    # This function is used to play the first 10 secondes of the correct answer of the questions of the quiz
    devices = sp.devices()
    for i in devices['devices']:
        device_id = i['id']
        break
    sp.start_playback(device_id=device_id, uris=track_uri)
    print('...PLAYING SONG FOR 10 SECONDES ON DEVICE')
    time.sleep(10)
    sp.pause_playback()


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
