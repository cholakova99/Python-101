import json
import random

class Song:
	def __init__(self,artist,title,album,length):
		if title is None or artist is None or album is None or length is None:
			raise AssertionError('Not all arguments were given!')
		if type(title) != str or type(artist) != str or type(album) != str or type(length) != str:
			raise ValueError('Wrong input! Use strings!')
		if title == "" or artist == "" or album == "" or length == "":
			raise ValueError('Empty string was given!')
		helper = length.split(":")
		if len(helper) == 0 or len(helper) > 3:
			raise ValueError('Wrong input for the length of the song')
		self.title = title
		self.artist = artist
		self.album = album
		self.length = length

	def __hash__(self):
		return hash((self.title,self.artist,self.album,self.length))

	def __eq__(self,other):
		if self.album == other.album and self.artist == other.artist and self.title == other.title:
			return True
		else:
			return False


	def __str__(self):
		return f'{self.artist} - {self.title} from {self.album} - {self.length}'

	def length_of_song(self,seconds=False,minutes=False,hours=False):
		helper = (self.length).split(":")
		if len(helper) == 2:
			hours_int = 0
			minutes_int = int(helper[0])
			seconds_int = int(helper[1])
		if len(helper) == 1:
			hours_int = 0
			minutes_int = 0
			seconds_int = int(helper[0])
		if len(helper) == 3:
			hours_int = int(helper[0])
			minutes_int = int(helper[1])
			seconds_int = int(helper[2])
		if seconds is False and minutes is False and hours is False:
			return self.__str__()
		if seconds is True:
			if minutes is True or hours is True:
				raise AssertionError('Only one argument could be true at the same time')
			else:
				value = 60*minutes_int + 60*60*hours_int + seconds_int
		if minutes is True:
			if seconds is True or hours is True:
				raise AssertionError('Only one argument could be true at the same time')
			else:
				value = 60*hours_int + minutes_int
		if hours is True:
			if seconds is True or minutes is True:
				raise AssertionError('Only one argument could be true at the same time')
			else:
				value = hours_int
		return value



class Playlist:
	list_of_songs = []
	def __init__(self,name,repeat=False,shuffle=False):
		if type(name) is not str:
			raise AssertionError('Name must be string!')
		self.name = name
		self.repeat = repeat
		self.shuffle = shuffle
		self.list_of_songs = []

	def __eq__(self,other):
		return self.name == other.name

	def add_song(self,song):
		if type(song) is not Song:
			raise AssertionError('Only songs could be added in the playlist')
		for i in range(0,len(self.list_of_songs)):
			if self.list_of_songs[i].__eq__(song):
				return f'this song is already in the playlist'
		self.list_of_songs.append(song)

	def add_songs(self,to_be_added):
		if type(to_be_added) is not list:
			raise ValueError('You should parse list only')
		for i in range(0,len(to_be_added)):
			self.add_song(to_be_added[i])
			i+=1

	def total_length(self):
		return len(self.list_of_songs)

	def artists_dic(self):
		autors_dict = {}
		for i in range(0,len(self.list_of_songs)):
			if self.list_of_songs[i].artist in autors_dict:
				autors_dict[self.list_of_songs[i].artist] +=1
			else:
				autors_dict[self.list_of_songs[i].artist] = 1
		return autors_dict

	def next_song(self):
		end = len(self.list_of_songs) - 1
		current_song_number = random.randint(0,end)
		if self.repeat = True:
			if end == current_song_number:
				return self.list_of_songs[0]
		if self.repeat = False:
			if end == current_song_number:
				return f'end of the playlist'
		return self.list_of_songs[current_song_number+1]


	def save(self):
		helper = self.name
		helper = helper.replace(" ","-")
		helper = json.dumps(self.list_of_songs)

	def load(self,path):
		with open(path,'r') as f:
			my_new_object = json.load(f)
			return my_new_object






	


	
	


