from billboard_manager import BillboardManager;
from spotify_manager import SpotifyManager;


billboard_data = BillboardManager();
all_songs = billboard_data.get_songs_name();
year = billboard_data.get_year();
print(year);

spotify_manager = SpotifyManager(song_list=all_songs, year=year);

spotify_manager.add_playlist();

