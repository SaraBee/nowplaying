import requests
import json

uri = 'https://api.wnyc.org/api/v1/whats_on/wqxr/'

class Radio:
    def fetchTrack():
        response = requests.get(uri)
        json = response.json()

        if 'current_playlist_item' in json and json['current_playlist_item'] != None:
            return json['current_playlist_item']
        elif 'current_show' in json:
            return json['current_show']

        return []


    def getTitle(track):
        if 'title' in track:
            return track['title']
        elif 'catalog_entry' in track and 'title' in track['catalog_entry']:
                return track['catalog_entry']['title']
        return ''

    def getComposer(track):
        if 'catalog_entry' in track and 'composer' in track['catalog_entry']:
            return track['catalog_entry']['composer']['name']
        return ''

    def getConductor(track):
        return track['conductor']['name']

    def getStartTime(track):
        # if there's an actual track
        if 'start_time_ts' in track:
            return track['start_time_ts']
        # if we're falling back on show
        elif 'start_ts' in track:
            return track['start_ts']
        return ''
