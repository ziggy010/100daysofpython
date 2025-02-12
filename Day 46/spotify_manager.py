import requests;
import spotipy;
from spotipy.oauth2 import SpotifyOAuth;


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='9feacf5c7a964a3f9cb37b424cd2003b', 
    client_secret='60387888fb4646cd8fbc7f9378f63528', 
    redirect_uri='http://example.com', 
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path='Day 46/token.txt',
    username='nut'
))

# user_id = sp.current_user();

name = "Lose Control";
year = "2025-01-10";

result = sp.search(q=f"track:{name} year:{2025}", type = 'track');

uri = result["tracks"]["items"][0]["uri"];

print(uri);
