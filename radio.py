import requests
import json

base_uri = 'https://api.prod.nypr.digital/api/v1'
now_playing_uri = '/whats_on/wqxr/3/'

class Radio:
    def fetch_track():
        uri = base_uri + now_playing_uri
        response = requests.get(uri)
        json = response.json()

        track = json['current_playlist_item']['catalog_entry']
        return track


    def get_title(track):
        return track['title']

    def get_composer(track):
        return track['composer']['name']

    def get_conductor(track):
        return track['conductor']['name']

track = Radio.fetch_track()
composer = Radio.get_composer(track)
title = Radio.get_title(track)

guess_composer = input("Who do you think the composer is? Guess: ")

composer_toks = composer.split(" ")
composer_last_tok = composer_toks.pop()

if guess_composer == composer or guess_composer == composer_last_tok:
    print("Correct! The piece is " + title + " by " + composer)
else:
    print("Whoops! The piece is " + title + " by " + composer)
