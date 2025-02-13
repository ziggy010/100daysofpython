import requests;
import spotipy;
from spotipy.oauth2 import SpotifyOAuth;

CLIENT_ID = '9feacf5c7a964a3f9cb37b424cd2003b';
scope = "playlist-read-private, " \
        "user-read-currently-playing, " \
        "user-read-currently-playing, " \
        "user-follow-read, playlist-modify-private"

class SpotifyManager:
    def __init__(self, song_list: list, year):
        self.year = year;
        self.song_list = song_list;
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id= CLIENT_ID,
            client_secret='60387888fb4646cd8fbc7f9378f63528', 
            redirect_uri='http://example.com', 
            scope=scope,
            show_dialog=True,
            cache_path='Day 46/token.txt',
        ));

        # user_id = sp.current_user();

    def get_song_uri(self):
        self.song_uri = [];
        for item in self.song_list:
            song_name = item;
            result = self.sp.search(q= f"track:{song_name} year:{self.year}", type='track');

            if result['tracks']['items']:
                self.song_uri.append(result['tracks']['items'][0]['uri']);
            else:
                print(f"{song_name} not found in spotify");
        


    def add_playlist(self):
        self.get_song_uri();
        current_user_details = self.sp.current_user();
        user_id = current_user_details['id'];
        print(user_id);
        playlist = self.sp.user_playlist_create(user=user_id, name=f"Billboard top 10 song of {self.year}", public=False);

        self.sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'], tracks=self.song_uri);


