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
