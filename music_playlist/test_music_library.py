import unittest
from mysic_library import Song, Playlist

class TestSong(unittest.TestCase):
	
	def test_empty_string(self):
		exc = None
		try:
			Song("armin van buren","mr.navigator","ultra europe","")
		except ValueError as error:
			exc = error
		self.assertIsNotNone(exc)

	def test_wrong_input_for_length(self):
		exc = None
		try:
			Song("armin van buren","mr.navigator","ultra europe","1:29:12:33")
		except ValueError as error:
			exc = error
		self.assertIsNotNone(exc)

	def test_wrong_input_type(self):
		exc = None
		try:
			Song("armin van buren","mr.navigator","ultra europe",6)
		except ValueError as error:
			exc = error
		self.assertIsNotNone(exc)

	def test_length_with_second(self):
		song = Song("armin van buren","mr.navigator","ultra europe","1:10:10")
		song2 = Song("armin van buren","mr.navigator","ultra europe","0:10:10")
		song3 = Song("armin van buren","mr.navigator","ultra europe","10:10")
		song4 = Song("armin van buren","mr.navigator","ultra europe","0:10")
		song5 = Song("armin van buren","mr.navigator","ultra europe","49")
		self.assertEqual(song.length_of_song(seconds=True),4210)
		self.assertEqual(song2.length_of_song(seconds=True),610)
		self.assertEqual(song3.length_of_song(seconds=True),610)
		self.assertEqual(song4.length_of_song(seconds=True),10)
		self.assertEqual(song5.length_of_song(seconds=True),49)

	def test_length_without_arguments(self):
		song = Song("armin van buren","mr.navigator","ultra europe","1:10:10")
		expected = "armin van buren - mr.navigator from ultra europe - 1:10:10"
		helper = song.length_of_song()
		self.assertEqual(helper,expected)

	def test_length_with_two_arguments(self):
		exc = None
		song = Song("armin van buren","mr.navigator","ultra europe","1:10:10")
		try:
			res = song.length_of_song(seconds=True,minutes=True)
		except AssertionError as error:
			exc = error
		self.assertIsNotNone(exc)

	def test_length_with_minutes(self):
		song = Song("armin van buren","mr.navigator","ultra europe","1:10:10")
		song2 = Song("armin van buren","mr.navigator","ultra europe","10:10")
		song3 = Song("armin van buren","mr.navigator","ultra europe","10")
		self.assertEqual(song.length_of_song(minutes=True),70)
		self.assertEqual(song2.length_of_song(minutes=True),10)
		self.assertEqual(song3.length_of_song(minutes=True),0)

	def test_length_with_hours(self):
		song = Song("armin van buren","mr.navigator","ultra europe","1:10:10")
		song2 = Song("armin van buren","mr.navigator","ultra europe","10:10")
		self.assertEqual(song.length_of_song(hours=True),1)
		self.assertEqual(song2.length_of_song(hours=True),0)

class TestPlaylist(unittest.TestCase):

	def test_add_already_excisted_song(self):
		song = Song("armin van buren","mr.navigator","ultra europe","1:10:10")
		song2 = Song("armin van buren","mr.navigator","ultra europe","1:10:10")
		playlist = Playlist("armin",repeat=True,shuffle=True)
		playlist.add_song(song)
		expected = "this song is already in the playlist"
		self.assertEqual(expected,playlist.add_song(song2))

	def test_add_song(self):
		song = Song("armin van buren","mr.navigator","ultra europe","1:10:10")
		playlist = Playlist("armin",repeat=True,shuffle=True)
		playlist.add_song(song)
		helper = False
		for i in range(0,len(playlist.list_of_songs)):
			if playlist.list_of_songs[i].__eq__(song):
				helper = True
		self.assertEqual(helper,True)

	def test_add_list_of_songs_with_already_excisted_song(self):
		song = Song("armin van buren","mr.navigator","ultra europe","1:10:10")
		playlist = Playlist("armin",repeat=True,shuffle=True)
		playlist.add_song(song)
		beginning_value = len(playlist.list_of_songs)
		song2 = Song("kasst","hell on earth","idk","7:20")
		song3 = Song("armin van buren","mr.navigator","ultra europe","1:10:10")
		list_to_be_added = []
		list_to_be_added.append(song2)
		list_to_be_added.append(song3)
		playlist.add_songs(list_to_be_added)
		self.assertEqual(beginning_value+1,len(playlist.list_of_songs))

	def test_add_list_of_songs(self):
		song = Song("armin van buren","mr.navigator","ultra europe","1:10:10")
		playlist = Playlist("armin",repeat=True,shuffle=True)
		playlist.add_song(song)
		beginning_value = len(playlist.list_of_songs)
		song2 = Song("kasst","hell on earth","idk","7:20")
		song3 = Song("armin van buren","turn it up","ultra europe","2:12")
		list_to_be_added = []
		list_to_be_added.append(song2)
		list_to_be_added.append(song3)
		playlist.add_songs(list_to_be_added)
		self.assertEqual(beginning_value+2,len(playlist.list_of_songs))

	def test_length_of_playlist(self):
		song = Song("armin van buren","mr.navigator","ultra europe","1:10:10")
		playlist = Playlist("armin",repeat=True,shuffle=True)
		playlist.add_song(song)
		song2 = Song("kasst","hell on earth","idk","7:20")
		song3 = Song("armin van buren","turn it up","ultra europe","2:12")
		list_to_be_added = []
		list_to_be_added.append(song2)
		list_to_be_added.append(song3)
		playlist.add_songs(list_to_be_added)
		self.assertEqual(3,playlist.total_length())

	def test_dict_of_artists(self):
		song = Song("armin van buren","mr.navigator","ultra europe","1:10:10")
		playlist = Playlist("armin",repeat=True,shuffle=True)
		playlist.add_song(song)
		song2 = Song("kasst","hell on earth","idk","7:20")
		song3 = Song("armin van buren","turn it up","ultra europe","2:12")
		list_to_be_added = []
		list_to_be_added.append(song2)
		list_to_be_added.append(song3)
		playlist.add_songs(list_to_be_added)
		expected = {'armin van buren' : 2, 'kasst':1}
		self.assertEqual(expected,playlist.artists_dic())

		
if __name__ == '__main__':
	unittest.main()
