"""
-----AUTHORIZATION FLOW-----
"""
import spotipy, requests, json, time, pandas as pd
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import random as random
import time as time

#create app in Spotify API website
# cid ="f3c61fa6846e4642a1dc44f1180bdf9b"
# secret = "3330958c61ac44b2aa185054d5fd9c15"

# def obtain_id():
#     query = "What is your Spotify ID ?  "
#     id = input(str(query))
#     if id == None:
#         id = "11100731824"
#     else continue
#     return id
#
# username = obtain_id()


def authorization():
    """FUNCTION ALLOWING THE AUTHORIZATION AND ACCESS TOKEN TO USER'S INFORMATION

        Prints:
        Instruction to be followed on the terminal, in order to complete
        the authorization flow successfully. 

        Returns:

        sp: spotipy object enabling multiple method CALLS

        token: authorization token, used for queries necessitating user's consent.
        It is used on several method calls throughout our quizz"""

    cid ="11e754c7548240e7a02e1b59ec07b2f9"
    secret = "c3922e0fbd1b4c57ba9f0c32366a7fe8"
    # cid = " 42d0aa9d98ef4d4ba6524cea55bbca52"
    # secret = "3c08275254aa4381be5198e756755211"
    username = "11670183"

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    scope = 'user-library-read playlist-read-private playlist-modify-private playlist-modify-public user-top-read user-read-recently-played user-read-playback-state user-read-playback-state user-read-currently-playing user-modify-playback-state streaming app-remote-control user-read-email user-read-private'
    redirect_uri = "http://localhost:8888"
    print("")
    print("")
    print("WELCOME TO OUR SPOTIFY QUIZ APP")
    print("In a few moments (10 secondes) a browser window will open inviting you to log into your spotify account. This is necessary in order to access the listening data. This data will stay on your computer and is not transmited to us.")
    print("Once you login and accept the permissions, the browser will redirect you to a URL that will probably create a (not accessible) error. This is normal, you simply need to copy the link in the URL bar and past it in this console.")
        # time.sleep(10)

    token = util.prompt_for_user_token(username, scope, cid, secret, redirect_uri)
    if token:
        sp = spotipy.Spotify(auth=token)
        # print('Spotify Token:  ', token)
    else:
        print("Can't get token for", username)

    return sp, token
