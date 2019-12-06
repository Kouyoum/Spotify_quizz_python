# QUIZZ
# Import of other project files
import Backend


# Other Imports
import spotipy, requests, json, time, pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import random as random
import time as time


toptrack = Backend.user_top_tracks()

def question1():
	i = random.randint(0,len(toptrack['Track']))
	song = toptrack['Track'][i]
	uri = toptrack['URI'][i]
	artist = toptrack["Artist"][i]
	genres = Backend.artist_api([toptrack['Artist ID'][i]])['Genres']# need the album_feature as a list
	print('--- Q U E S T I O N  1 ---')
	print("We will start with an easy one. Among your 50 top played tracks, we choose one at random.")
	print("The random track is: ")
	print('     ',song,' ,', artist)
	print('What is one of the genres of this song ?')
	sentence = "One of the genre of ", song, " is:"
	u_input = input(str(sentence) )
	if u_input in str(genres):
		print('CORRECT')
		print(genres)
		# playback10s([uri])
		return 1
	else:
		print("INCORRECT")
		print(genres)
		# playback10s([uri])
		return 0


def question2():

	return


def question3():
	print('')
	print("")
	print("")
	print('--- Q U E S T I O N  2 ---')
	print("Among those 4 artists, who do you think is the most popular artist on Spotify ?")

	row = 0
	top_p = 0
	for i in range(0,len(toptrack['Artist'])):
		if int(toptrack['Popularity'][i]) >= top_p:
			row = i
			top_p = int(toptrack['Popularity'][i])
	uri = toptrack['URI'][row]
	artists = [random.randint(0,50) for i in range(4)]
	for i in artists:
		print(toptrack['Artist'][i])
	print(toptrack['Artist'][row])
	u_input = input('The most popular artist is: ')
	if u_input == toptrack['Artist'][row]:
		print('CORRECT')
		print(toptrack['Artist'][row], ' has a popularity of ', toptrack['Popularity'][row])
		# playback10s([uri])
		return 1
	else:
		print("INCORRECT")
		print(toptrack['Artist'][row], 'is the most popular artist with a popularity of ', toptrack['Popularity'][row])
		# playback10s([uri])
		return 0
	return


def question5():
	print("")
	print("")
	print("")
	print('--- Q U E S T I O N  3 ---')
	row = random.randint(0,len(toptrack['Track']))
	uri = toptrack['URI'][row]
	sentence = "In which year was the album ", toptrack['Album Name'][row], ' from ', toptrack['Artist'][row],  ' released ?'
	u_input = input(str(sentence))
	if u_input == toptrack['Album Year'][row]:
		print('CORRECT')
		print(toptrack['Album Year'][row], ' is the correct year for the album ', toptrack['Album Name'][row])
		# playback10s([uri])
		return 1
	else:
		print("INCORRECT")
		print(toptrack['Album Name'][row], ' was released in ', toptrack['Album Year'][row])
		# playback10s([uri])
		return 0

def question6():
	print("")
	print("")
	print("")
	print('--- Q U E S T I O N  4 ---')
	sentence = "Spotify creates a song characteristic named danceability that quantifies the danceability of the song. Among your top tracks, what is the name of the most danceable ?"
	# We get the Track ID with the highest level of Danceability.
	most_danceable_id = Backend.audio_features(toptrack['Track ID']).nlargest(1, "Danceability")['Track ID']
	# We need to join this Track ID with the track ID of the "tracks" API call in order to get the name of the song
	most_danceable = pd.merge(most_danceable_id,Backend.tracks(most_danceable_id),left_on='Track ID', right_on='Track ID',how='left')
	track_name = most_danceable['Track Name'][0]

	for i in range(4):
		r = random.randint(0,len(toptrack['Track ID']))
		print(toptrack['Track'][r])
	print(track_name)
	u_input = input(str(sentence))

	if u_input == track_name:
		print('CORRECT')
		print(track_name, ' is the most danceable')
		return 1
	else:
		print("INCORRECT")
		print(track_name, 'is the most danceable')
		return 0




q1 = question1()
# # question2()
q3 = question3()
q5 = question5()
q6 = question6()

correct = q1+q3+q5+q6
incorrect = 4-correct
print("")
print('')
print('YOU MADE ',incorrect, ' MISTAKES')

#export_csv()
#create_playlist()

print('THE END')

# #if __name__ = "__main__":
#

"""
Add ability to export to csv their private data

    """
