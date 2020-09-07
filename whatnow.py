from inky.auto import auto
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from radio import Radio
import sys
import os
import json

def formatLine(msg):
    global lines
    w, h = font.getsize(msg)
    if w <= inky_display.WIDTH - margin:
        # cool cool, the line fits, no split necessary
        lines.append(msg)
    else:
        toks = msg.split()
        cur_line = ''
        for tok in toks:
            cur_w, _ = font.getsize(cur_line + tok + ' ')
            if cur_w <= inky_display.WIDTH - margin:
                cur_line = cur_line +  tok + ' '
            else:
                lines.append(cur_line)
                # current token would put us over, start the next line with it
                cur_line = tok + ' '
        lines.append(cur_line)

inky_display = auto()
inky_display.set_border(inky_display.WHITE)
# Force b&w mode for speedy redraws
inky_display.colour = 'black'
inky_display.lut = 'black'


# set layout values for inkywHAT and inkypHAT
if inky_display.HEIGHT == 300:
    img = Image.open(os.path.join(current_dir, "whatnow.png")).resize(inky_display.resolution)
    font_size = 32
    margin = 40
else:
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    font_size = 20
    margin = 0


current_dir = os.path.dirname(__file__)

draw = ImageDraw.Draw(img)

font = ImageFont.truetype(FredokaOne, font_size)

lines = []

track = Radio.fetchTrack()
if not track:
    sys.exit()

composer = Radio.getComposer(track)
title = Radio.getTitle(track)

cache_file = '/tmp/cache'

last_track = ''

if os.path.exists(cache_file):
    cache = open(cache_file, 'rt')
    play_history = json.loads(cache.readline())
    cache.close()

    if play_history['current_track'] == composer + ' ' + title:
        print("skipping " + composer + ' ' + title)
        # No need to update the display, it's already up to date
        sys.exit()

    if play_history['last_track'] == composer + ' ' + title:
        print("WQXR is doing that thing again, skipping " + composer + ' ' + title)
        # Sometimes the API mysteriously returns the previous track after returning the correct one
        sys.exit()

    # time to do the shuffle, current track is now last track
    last_track = play_history['current_track']

# We open the cache file a second time in w mode to overwrite
cache = open(cache_file, 'w+')
play_history = {'last_track': last_track, 'current_track': composer + ' ' + title}
cache.write(json.dumps(play_history))
cache.close()

formatLine(Radio.getComposer(track))
formatLine(Radio.getTitle(track))

# approximate centered y is true center minus half lines * line height
_, line_height = font.getsize(lines[0])
centered_y = (inky_display.HEIGHT / 2) - ((line_height * len(lines)) / 2)

height_counter = centered_y
for i in range (0, len(lines)):
    msg = lines[i]
    w, h = font.getsize(msg)

    # approximate centered x is true center minus half line length
    x = (inky_display.WIDTH / 2) - (w / 2)
    y = height_counter
    draw.text((x, y), msg, inky_display.BLACK, font)
    height_counter += h

inky_display.set_image(img)
inky_display.show()
