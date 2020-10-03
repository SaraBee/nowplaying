from radio import Radio

track = Radio.fetchTrack()
if track:
    composer = Radio.getComposer(track)
    title = Radio.getTitle(track)

    if composer:
        print(composer + " - " + title)
    else:
        print(title)
else:
    print("Special Programming")
