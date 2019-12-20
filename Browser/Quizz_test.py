# QUIZZ
# Import of other project files
import Backend
import authorization as aut


# Other Imports
import spotipy, requests, json, time, pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import random
import time as time

# modules for string matching
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


toptrack = Backend.user_top_tracks()



# Question 1_a returns the correct genres to the question

def question1_a():
	""" Find the genres of a track

	Returns:
	Genres[0]: list of a track's genres (e.g. ['rock', 'hip hop'])

	id: the id of the track (useful to display the spotify player of the track)

	track: track name

	artist: artist name
	"""
	i = random.randint(0,len(toptrack['Track']))
	track = toptrack['Track'][i]
	uri = toptrack['URI'][i]
	id = toptrack['Track ID'][i]
	artist = toptrack['Artist'][i]
	genres = Backend.artist_api([toptrack['Artist ID'][i]])['Genres']# need the album_feature as a list
	#genres = genres_series.tolist()

	return genres[0], id, track, artist

# test1, test2, test3, test4 = question1_a()
# print(test1, "\n", test2, "\n", test3, test4)
# print(type(test1))


# Question 1_b returns the ratio of similarity between user input and response
def question1_b(answers, correct):
	"""		Compute the ratio of similarity between user's guess and solution

	 Args:
	 answers: user answer, string variable

	 correct: list of correct answers (here the genres of a spotify track)

	 Returns:
	 list of ratios of similarity between the user's 3 guesses and the solutions.
	 """
	# Transform user's answer into a list
	answers_l = answers.split(',')

	# Transform user's answers into a list
	ratio = []
	for answer in answers_l:
		for option in correct:
			grade = fuzz.partial_ratio(option, answers_l)
			ratio.append(grade)
		# if grade > 80:
		# 	return "correct"
	return ratio

# ratio = question1_b(answers1, test1)
# print(ratio)

#genres, ratio = question1()
#print(genres, ratio)



def question2():
	# 4 tracks picked randomly out of the user's 50 most heard tracks
	sample_songs = toptrack.loc[random.sample(range(0, 49), 4), ["Track", "Popularity", "Artist", "Track ID"]]

	# Obtain the most popular song in from the random sample
	most_danceable = sample_songs['Track'][sample_songs['Popularity'].idxmax()]

	# Obtain the song's id, for the player to work
	index = sample_songs.loc[sample_songs['Track']== most_danceable].index[0]
	id_mostd = sample_songs['Track ID'][index]

	sample_songs["Popularity"] = pd.to_numeric(sample_songs["Popularity"])

	sample_artists = list(sample_songs['Artist'])
	sample_names = list(sample_songs['Track'])

	# list of tracks with the artists names
	for i in range(len(sample_names)):
		sample_names[i] += " by " + sample_artists[i]


	return sample_names, sample_artists, most_danceable, id_mostd

# sample_songs, most_danceable, id = question2()
# print(sample_songs, most_danceable)
# print(type(id))



def question3():
	"""
	QUESTION ON THE ALBUM YEAR

	Picks a random track out of the user's top50
	and asks when the album including the track was composed.

	Returns:
	album_name: string variable, name of the album

	artist name: string variable, name of the artist

	sample_year: list of years (1 correct answer & 3 random years)

	correct year: integer variable, correct year for album composition

	track_id: id of the song, belonging to the album
	(used for the spotify player later)

	"""
	row = random.randint(0,len(toptrack['Track']))
	uri = toptrack['URI'][row]

	# Get the album, artist name, and track id from the dataframe
	album_name = toptrack['Album Name'][row]
	artist_name = toptrack['Artist'][row]
	track_id = toptrack['Track ID'][row]

	# Set year to integer, to manipulate it
	correct_year = int(toptrack['Album Year'][row])
	sample_year = random.sample(range(correct_year-20, 2019), 3)

	sample_year.append(correct_year)

	return album_name, artist_name, sample_year, correct_year, track_id



def question4():
	"""
	QUESTION ON EXPLICIT CONTENT IN SONGS

	Counts the number of tracks with explicit content, from the user's top 50.

	Returns:
	sample_count: list of 4 integers, 4 options for the multiple choice

	explicit_count: integer, number of explicit songs in the user's top 50

	"""
	# 3 datafframes created: 4 tracks, explicit tracks, implicit
	explicit_df = toptrack.loc[toptrack["Explicit"] == True]
	explicit_count = len(explicit_df)
	sample_count = random.sample(range(0, explicit_count + 5), 3)

	sample_count.append(explicit_count)

	return explicit_count, sample_count


def question6():
	"""
	QUESTION ON DANCEABILITY

	Returns:
	sample_names: list of 4 tracks from the user's top 50, randomly chosen

	most_danceable: string variable, name of the track scoring the
	highest in terms of danceability

	track_id: id of the most danceable track, used for the spotify player later
	"""
	Track_id = Backend.audio_features(toptrack['Track ID'])
	sample_tracks = Track_id.loc[random.sample(range(0, 49), 4), ["Track ID", "Danceability"]] # 4 random tracks IDs & Danceabilityy

	# We need to join the 2 dataframes in order to get the name of the songs
	Track_full = pd.merge(sample_tracks,Backend.tracks(sample_tracks["Track ID"]),left_on='Track ID', right_on='Track ID',how='left')

	# new dataframe created, with only 3 columns
	sample_tracks = Track_full.loc[:,['Track Name', 'Danceability', 'Track ID']]

	# list of track options names
	sample_names = list(sample_tracks['Track Name'])
	most_danceable = sample_tracks['Track Name'][sample_tracks['Danceability'].idxmax()]

	# obtain the id for the most danceable track
	track_id = sample_tracks['Track ID'][sample_tracks['Track Name'] == most_danceable].values[0]

	return sample_names, most_danceable, track_id





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
