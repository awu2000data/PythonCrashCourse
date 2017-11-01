"""
Exercise 8-7
Write a function called make_album() that
builds a dictionary with an artist name and album title.
Use the function to build three dictionaries
and then print them all.

Add an optional parameter to store the number of tracks
Make one new call with the optional parameter
"""

def make_album(artist_name, album_title, number_of_tracks=""):
	album = {"artist": artist_name, "album": album_title}
	if number_of_tracks:
		album['tracks'] = number_of_tracks
	return album

album = make_album("Blink-182", "California")
print(album)
album = make_album("Lorde", "Pure Heroine")
print(album)
album = make_album("Drake", "Take Care")
print(album)
album = make_album("Kid Cudi", "Indicud", 18)
print(album)