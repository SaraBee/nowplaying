from inky.auto import auto
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from radio import Radio
import sys
import os

def formatLine(msg):
    global lines
    w, h = font.getsize(msg)
    if w <= inky_display.WIDTH - 40:
        # cool cool, the line fits, no split necessary
        lines.append(msg)
    else:
        toks = msg.split()
        cur_line = ''
        for tok in toks:
            cur_w, _ = font.getsize(cur_line + tok + ' ') 
            if cur_w <= inky_display.WIDTH - 40:
                cur_line = cur_line +  tok + ' '
            else:
                lines.append(cur_line)
                # current token would put us over, start the next line with it
                cur_line = tok + ' '
        lines.append(cur_line)

inky_display = auto()
inky_display.set_border(inky_display.WHITE)

current_dir = os.path.dirname(__file__)

#img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
img = Image.open(os.path.join(current_dir, "whatnow.png")).resize(inky_display.resolution)
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(FredokaOne, 32)

lines = []

track = Radio.fetchTrack()
if not track:
    sys.exit()

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
