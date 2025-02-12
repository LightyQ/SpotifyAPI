import spotipy
from spotipy.oauth2 import SpotifyOAuth
from colorama import Fore, Style, init

init(autoreset=True)

# Spotify API credentials
CLIENT_ID = "YOUR_CLIENT_ID"  # Replace with your Spotify Client ID
CLIENT_SECRET = "YOUR_CLIENT_SECRET"  # Replace with your Spotify Client Secret
REDIRECT_URI = "http://localhost:8888/callback/"  # Redirect URI configured in Spotify Developer Dashboard (ALWAYS SET TO LOCALHOST)

SCOPE = "user-follow-read"

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

# Get the current user's profile
def get_user_profile():
    user = sp.current_user()
    print(f"{Fore.RED}--- User Profile ---{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Display Name:{Style.RESET_ALL} {user['display_name']}")
    print(f"{Fore.GREEN}User ID:{Style.RESET_ALL} {user['id']}")
    print(f"{Fore.GREEN}Followers:{Style.RESET_ALL} {user['followers']['total']}")
    print(f"{Fore.GREEN}Profile URL:{Style.RESET_ALL} {user['external_urls']['spotify']}")

# Get all playlists the user owns or follows
def get_user_playlists():
    playlists = sp.current_user_playlists()
    print(f"{Fore.RED}--- User Playlists ---{Style.RESET_ALL}")
    for playlist in playlists['items']:
        print(f"{Fore.YELLOW}- {playlist['name']} {Style.RESET_ALL}"
              f"(Tracks: {playlist['tracks']['total']}, "
              f"ID: {Fore.LIGHTMAGENTA_EX}{playlist['id']}{Style.RESET_ALL})")
    print("\n")

# Get detailed information about a specific playlist
def get_playlist_details(playlist_id):
    playlist = sp.playlist(playlist_id)
    print(f"{Fore.RED}--- Playlist Details ---{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Name:{Style.RESET_ALL} {playlist['name']}")
    print(f"{Fore.GREEN}Description:{Style.RESET_ALL} {playlist['description']}")
    print(f"{Fore.GREEN}Owner:{Style.RESET_ALL} {playlist['owner']['display_name']}")
    print(f"{Fore.GREEN}Followers:{Style.RESET_ALL} {playlist['followers']['total']}")
    print(f"{Fore.RED}Tracks:{Style.RESET_ALL}")
    for item in playlist['tracks']['items']:
        track = item['track']
        print(f"{Fore.YELLOW}- {track['name']} {Style.RESET_ALL}"
              f"by {Fore.LIGHTBLUE_EX}{', '.join([artist['name'] for artist in track['artists']])}{Style.RESET_ALL}")
    print("\n")

if __name__ == "__main__":
    print(f"{Fore.MAGENTA}Fetching Spotify Account Information...{Style.RESET_ALL}\n")
    get_user_profile()
    get_user_playlists()

    # Specify a playlist ID to get its details
    playlist_id = input(f"{Fore.RED}Enter a playlist ID to fetch details:{Style.RESET_ALL} ")
    get_playlist_details(playlist_id)
