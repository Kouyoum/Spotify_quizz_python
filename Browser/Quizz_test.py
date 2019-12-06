# QUIZZ
# Import of other project files
import Backend


# Other Imports
import spotipy, requests, json, time, pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import random
import time as time


toptrack = Backend.user_top_tracks()
#summary = toptrack.loc[:,['Track', 'Artist', 'Explicit', 'Album Name', 'Album Year']]
#print(summary)
# def question1():
# 	i = random.randint(0,len(toptrack['Track']))
# 	song = toptrack['Track'][i]
# 	uri = toptrack['URI'][i]
# 	artist = toptrack["Artist"][i]
# 	genres = Backend.artist_api([toptrack['Artist ID'][i]])['Genres']# need the album_feature as a list
# 	print('--- Q U E S T I O N  1 ---')
# 	print("For this first question, we will start with an easy one. Among your 50 top played tracks, we choose one at random.")
# 	print("The random track is: ")
# 	print('     ',song,' ,', artist)
# 	print('What is one of the genres of this song ?')
# 	sentence = "One of the genre of ", song, " is:"
# 	u_input = input(str(sentence) )
# 	if u_input in str(genres):
# 		print('CORRECT')
# 		print(genres)
# 		# playback10s([uri])
# 		return 1
# 	else:
# 		print("INCORRECT")
# 		print(genres)
# 		# playback10s([uri])
# 		return 0

#question1()
#
#
# def question2():
#
# 	return
#
#
def question2():
	# print("Among those 4 tracks, who do you think is the most popular on Spotify ?")
	sample_songs = toptrack.loc[random.sample(range(0, 49), 4), ["Track", "Popularity", "Artist", "Track ID"]]

	# Obtain the most popular song in from the random sample
	most_danceable = sample_songs['Track'][sample_songs['Popularity'].idxmax()]

	# Obtain the song's id, for the player to work
	ind = sample_songs.loc[sample_songs['Track']== most_danceable].index[0]
	id_mostd = sample_songs['Track ID'][ind]

	sample_songs["Popularity"] = pd.to_numeric(sample_songs["Popularity"])

	#sample_artists = list(sample_songs['Artist'])
	sample_names = list(sample_songs['Track'])

	return sample_names, most_danceable, id_mostd

# sample_songs, most_danceable, id = question2()
# print(sample_songs, most_danceable)
# print(type(id))


"""Takes a random track out of the 50 tracks most heard. Returns album, artist name,
correct year and a list of 4 possible years, for the multiple choice quizz"""
def question3():
	row = random.randint(0,len(toptrack['Track']))
	uri = toptrack['URI'][row]

	# Get the album and artist name from the dataframe
	album_name = toptrack['Album Name'][row]
	artist_name = toptrack['Artist'][row]

	# Set year to integer, to manipulate it
	correct_year = int(toptrack['Album Year'][row])
	sample_year = random.sample(range(correct_year-20, 2019), 3)

	sample_year.append(correct_year)

	# sentence = "In which year was the album ", toptrack['Album Name'][row], ' from ', toptrack['Artist'][row],  ' released ?'
	# u_input = input(str(sentence))
	return album_name, artist_name, sample_year, correct_year

# track, artist, sample, correct  = question5()
# print("{} by {} in {}".format(track, artist, correct))
# print(sample)
# 	if u_input == toptrack['Album Year'][row]:
# 		print('CORRECT')
# 		print(toptrack['Album Year'][row], ' is the correct year for the album ', toptrack['Album Name'][row])
# 		# playback10s([uri])
# 		return 1
# 	else:
# 		print("INCORRECT")
# 		print(toptrack['Album Name'][row], ' was released in ', toptrack['Album Year'][row])
# 		# playback10s([uri])
# 		return 0
#

# CRash test for flask
# def question6():
# 	sentence = "Spotify creates a song characteristic named danceability that quantifies the danceability of the song. Among your top tracks, what is the name of the most danceable ?"
# 	# We get the Track ID with the highest level of Danceability.
#
# 	most_danceable_id = Backend.audio_features(toptrack['Track ID']).nlargest(1, "Danceability")['Track ID']
# 		# We need to join this Track ID with the track ID of the "tracks" API call in order to get the name of the song
# 	#most_danceable = pd.merge(most_danceable_id,Backend.tracks(most_danceable_id),left_on='Track ID', right_on='Track ID',how='left')
# 	most_danceable = pd.merge(most_danceable_id,Backend.tracks(most_danceable_id),left_on='Track ID', right_on='Track ID',how='left')
# 	track_name = most_danceable['Track Name'][0]
# 	# We need to join this Track ID with the track ID of the "tracks" API call in order to get the name of the song
# 	most_danceable = pd.merge(most_danceable_id,Backend.tracks(most_danceable_id),left_on='Track ID', right_on='Track ID',how='left')
# 	track_name = most_danceable['Track Name'][0]
#
# 	choices = []
# 	for i in range(4):
# 		r = random.randint(0,len(toptrack['Track ID']))
# 		choices.append(toptrack['Track'][r])
#
# 	choices.append(track_name)
# 	return choices


def question6():
	Track_id = Backend.audio_features(toptrack['Track ID'])
	sample_tracks = Track_id.loc[random.sample(range(0, 49), 4), ["Track ID", "Danceability"]] # 4 random tracks IDs & Danceabilityy

	# We need to join this Track ID with the track ID of the "tracks" API call in order to get the name of the song

	Track_full = pd.merge(sample_tracks,Backend.tracks(sample_tracks["Track ID"]),left_on='Track ID', right_on='Track ID',how='left')

	sample_tracks = Track_full.loc[:,['Track Name', 'Danceability']]
	# list of track options names
	sample_names = list(sample_tracks['Track Name'])
	most_danceable = sample_tracks['Track Name'][sample_tracks['Danceability'].idxmax()]

	return sample_names, most_danceable

# sample_names, most_danceable = question6()
# print(sample_names)
# print(most_danceable)



# # #
# # #
# # # q1 = question1()
# # # # # question2()
# # # q3 = question3()
# # # q5 = question5()
# # # q6 = question6()
# # #
# # # correct = q1+q3+q5+q6
# # # incorrect = 4-correct
# # # print("")
# # # print('')
# # # print('YOU MADE ',incorrect, ' MISTAKES')
# # #
# # # #export_csv()
# # # #create_playlist()
# # #
# # # print('THE END')
# # #
# # # # #if __name__ = "__main__":
# # # #
# # #
# # # """
# # # Add ability to export to csv their private data
# # #
# # #     """

# if __name__ == "__main__":
# 	print("Quizz_test imported")
