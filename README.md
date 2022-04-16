# SpotifyrankProject

This project is designed to take in a song, and visualize how Spotify ranks the audio features of that song. This project was made with the help of the SpotifyWebAPI, so the input needs to be a Spotify URL of the song. This was a quick project done in under a week, as a way to apply what I had learned outside and inside my classes, and I also learned a lot of new things.




To run the project you will need to set up a couple enviroment variables beforehand.

1)FLASK_APP='app', which will tell Flask what python file to run.

2)FLASK_ENV='development', which will tell Flask what mode to run on.

3)SECRET_KEY="5f358909324c22463451387a0aec5d2f", which is the secret_key needed for Flask.

4)SPOTIPY_CLIENT_ID='f907777e21da4340b790270291800875', which is used for the SpotifyAPI.

5)SPOTIPY_CLIENT_SECRET='3cff1234c4454f669addc3daf116cf0c', which is also used for the SpotifyAPI.

(The information for the enviromental variables are all examples, so one will need to provide one's personal information for it to work.)

To get the information for the SpotifyAPI client_id and client_secret follow these steps:https://developer.spotify.com/documentation/general/guides/authorization/app-settings/
