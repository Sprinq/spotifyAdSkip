import time
import subprocess
import pyautogui
import psutil
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace these with your own credentials
SPOTIPY_CLIENT_ID = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'
SPOTIPY_REDIRECT_URI = 'your_redirect_uri'

scope = 'user-read-playback-state user-modify-playback-state'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))
def is_ad_playing():
    current_playback = sp.current_playback()
    if current_playback and current_playback['currently_playing_type'] == 'ad':
        return True
    return False

def close_spotify():
    for proc in psutil.process_iter():
        if proc.name().lower() == "spotify.exe":
            proc.kill()

def reopen_spotify():
    subprocess.Popen([r"C:/path/to/Spotify.exe"])  # Update with your Spotify path
    time.sleep(5)  # Wait for Spotify to open

def press_play_button():
    time.sleep(2)  # Wait for the app to be ready
    pyautogui.press('space')  # Press space to play

def main():
    while True:
        if is_ad_playing():
            print("Ad detected, closing Spotify...")
            time.sleep(2)
            close_spotify()
            print("Reopening Spotify...")
            reopen_spotify()
            print("Pressing play button...")
            press_play_button()
        time.sleep(3)  # Check every 3 seconds

if __name__ == "__main__":
    main()
