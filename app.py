from flask import Flask, render_template, request, url_for, flash, redirect
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import os

app = Flask(__name__)
SECRET_KEY = os.environ.get("SECRET_KEY")
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=('Get', 'Post'))
def index():
    post = {}
    if request.method == 'POST':
        url = request.form['urlInput']
        # getting the api token
        auth_manager = SpotifyClientCredentials()
        sp = spotipy.Spotify(auth_manager=auth_manager)
        # Getting the audio features from the inputted url and making sure it is valid.
        if sp.audio_features(url) == [None]:
            flash("""That doesn't seem to be a valid url. For help finding the 
            appropriate url click on the link below.""")
        else:
            audio_features = sp.audio_features(url)
            df = pd.DataFrame(audio_features)
            danceability = df["danceability"]
            energy = df["energy"]
            loudness = df["loudness"]*-1
            speechiness = df["speechiness"]
            acousticness = df["acousticness"]
            instrumentalness = df["instrumentalness"]
            liveness = df["liveness"]
            valence = df["valence"]
            tempo = df["tempo"]
            df_af = {"danceability":danceability[0], "energy":energy[0], 
            "loudness":loudness[0], "speechiness":speechiness[0], 
            "acousticness":acousticness[0], "instrumentalness":instrumentalness[0], 
            "liveness":liveness[0], "valence":valence[0], "tempo":tempo[0]}
            post = df_af
    return render_template('index.html', post=post)

@app.route('/info')
def info():
    return render_template('info.html')
