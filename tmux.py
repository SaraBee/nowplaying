from radio import Radio

track = Radio.fetch_track()
composer = Radio.get_composer(track)
title = Radio.get_title(track)

print(composer + " - " + title)
