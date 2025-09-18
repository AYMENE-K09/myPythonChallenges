class PlaylistManager:
    def __init__ (self, playlist_name):
        self.playlist_name = playlist_name
        self.songs = [] #empty list to store song names

    def add_song(self, new_song):
        if new_song not in self.songs:
            self.songs.append(new_song)
            print(f"'{new_song}' was added to {self.playlist_name} playlist")
        else:
            print(f"'{new_song}' already existe in {self.playlist_name} playlist")


    def remove_song(self, song_name):
        if song_name in self.songs:
            self.songs.remove(song_name)
            print(f"the '{song_name}' was removed from {self.playlist_name} playlist")
        else:
            print(f"the '{song_name}' is not exist in {self.playlist_name} playlist")

    def show_playlist(self):
        print(self.songs)

    def sort_by_genre(self,):
        self.song_group = {}
        for song in self.songs:
            song_info = song.split("-")
            song_genre = song_info[2].strip()
            if song_genre not in self.song_group:
                self.song_group[song_genre] = [song]

            else:
                self.song_group[song_genre].append(song)

        print(self.song_group)
    
    def play_next(self):
        if not self.songs:
            return "The playlist is empty!"
        
        else:
            next_song = self.songs[0]
            self.songs.remove(next_song)
            return f"Now playing: {next_song}"
        

my_playlist = PlaylistManager("My Mix")
my_playlist.add_song("Bohemian Rhapsody - Queen - Rock")
my_playlist.add_song("Halo - Beyoncé - Pop")
my_playlist.add_song("Bad Guy - Billie Eilish - Pop")
my_playlist.add_song("Sweet Child o' Mine - Guns N' Roses - Rock")
my_playlist.remove_song("Bad Guy - Billie Eilish - Pop")
my_playlist.show_playlist()
my_playlist.sort_by_genre()
print(my_playlist.play_next())
