# Windows Spotify Ad Skipper

This Python script created mostly by ChatGPT detects when an ad is playing on Spotify, closes the Spotify application, reopens it, and resumes playback. It utilizes the Spotify Web API to detect ads and uses system commands to control the Spotify application.

## Requirements

1. **Spotify Developer Account**: You need to create an application in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) to get your `client_id` and `client_secret`.
2. **Python Packages**: Install the following Python libraries:
   - `spotipy`: For interacting with the Spotify API.
   - `pyautogui`: For simulating key presses.
   - `psutil`: For managing system processes.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Sprinq/spotifyAdSkip.git
   cd spotify-ad-skipper
2. **Install Dependencies**:
   ```bash
   pip install spotipy pyautogui psutil
3. **Set Up Your Spotify App**:
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications), create an app, and get your `client_id` and `client_secret`.
   - Set a redirect URI in the app settings and use the same URI in your script. You can use "http://localhost:8080/" for the URI.

## Configuration

1. **Update the Script with Your Credentials**:
   - Open the `ad_skip.py` file.
   - Replace the placeholders with your Spotify app credentials:
     ```python
     SPOTIPY_CLIENT_ID = 'your_client_id'
     SPOTIPY_CLIENT_SECRET = 'your_client_secret'
     SPOTIPY_REDIRECT_URI = 'your_redirect_uri'
     ```

2. **Update the Path to Spotify Executable**:
   - Update the path to your Spotify executable in the `reopen_spotify` function:
     ```python
     subprocess.Popen([r"C:/path/to/Spotify.exe"])  # Update with your Spotify path
     ```

## Optional: Minimize Spotify

   - Uncomment these two lines from the press_play_button() function seen below
     ```python
     #pyautogui.hotkey('alt', 'space')  # Open the window menu
     #pyautogui.press('n')  # Press 'n' to minimize
     ```

## Usage

1. **Run the Script**:
   ```bash
   python ad_skip.py
## How It Works
- The script will continuously check if an ad is playing every 3 seconds.
- If an ad is detected, it will close the Spotify application.
- It will then reopen Spotify and press the play button to resume playback.
- (Optional) It will minimize Spotify after resuming playback.

## Troubleshooting

- **Authentication Issues**: Ensure that your `client_id`, `client_secret`, and `redirect_uri` are correctly set up in the Spotify Developer Dashboard and in your script.
- **Path to Spotify**: Ensure the path to the Spotify executable is correct. Update it as needed in the `reopen_spotify` function.
- **Dependencies**: Make sure all required Python libraries are installed.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
