from radio import Radio

track = Radio.fetchTrack()
if track:
    composer = Radio.getComposer(track)
    title = Radio.getTitle(track)

    print(composer + " - " + title)
else:
    print("Special Programming")
