from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from radio import Radio
import sys
import os

def formatLine(msg):
    global lines
    w, h = font.getsize(msg)
    if w <= inky_display.WIDTH:
        # cool cool, the line fits, no split necessary
        lines.append(msg)
    else:
        toks = msg.split()
        cur_line = ''
        for tok in toks:
            cur_w, _ = font.getsize(cur_line + tok + ' ') 
            if cur_w <= inky_display.WIDTH:
                cur_line = cur_line +  tok + ' '
            else:
                lines.append(cur_line)
                # current token would put us over, start the next line with it
                cur_line = tok + ' '
        lines.append(cur_line)

inky_display = InkyPHAT('black')
inky_display.set_border(inky_display.WHITE)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(FredokaOne, 20)

lines = []

track = Radio.fetchTrack()
if not track:
    sys.exit()

current_dir = os.path.dirname(__file__)
cache_file = os.path.join(current_dir, 'cache')

cache = open(cache_file, 'rt')
last_track = cache.readline()
cache.close()

composer = Radio.getComposer(track)
title = Radio.getTitle(track)

if last_track == composer + ' ' + title:
    print("skipping " + composer + ' ' + title)
    # No need to update the display, it's already up to date
    sys.exit()

# We open the cache file a second time in w mode to overwrite
cache = open(cache_file, 'w')
cache.write(composer + ' ' + title)
cache.close()

formatLine(Radio.getComposer(track))
formatLine(Radio.getTitle(track))

height_counter = 0
for i in range (0, len(lines)):
    msg = lines[i]
    w, h = font.getsize(msg)
    x = 0
    y = height_counter
    draw.text((x, y), msg, inky_display.BLACK, font)
    height_counter += h

inky_display.set_image(img)
inky_display.show()
