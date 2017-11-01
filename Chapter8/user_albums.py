"""
Exercise 8-8
Start with your program from 8-7
Write a while loop that allows users to input an
album's artist and title.  
Call the function and make the album
"""

def make_album(artist_name, album_title, number_of_tracks=""):
	album = {"artist": artist_name, "album": album_title}
	if number_of_tracks:
		album['tracks'] = number_of_tracks
	return album

while True:
	print("\nEnter 'q' to quit")
	artist = input("Artist Name: ")
	if artist == 'q':
		break
	title = input("Album Title: ")
	if title == 'q':
		break
	album = make_album(artist, title)
	print(album)
	
