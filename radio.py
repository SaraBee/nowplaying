import requests
import json

base_uri = 'https://api.prod.nypr.digital/api/v1'
now_playing_uri = '/whats_on/wqxr/3/'

class Radio:
    def fetchTrack():
        uri = base_uri + now_playing_uri
        response = requests.get(uri)
        json = response.json()

        if json['current_playlist_item'] != None:
            return json['current_playlist_item']['catalog_entry']

        return []


    def getTitle(track):
        return track['title']

    def getComposer(track):
        return track['composer']['name']

    def getConductor(track):
        return track['conductor']['name']
