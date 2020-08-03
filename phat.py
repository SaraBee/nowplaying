from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from radio import Radio

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

inky_display = InkyPHAT("yellow")
inky_display.set_border(inky_display.WHITE)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(FredokaOne, 18)

lines = []

track = Radio.fetchTrack()
if track:
    formatLine(Radio.getComposer(track))
    formatLine(Radio.getTitle(track))

for i in range (0, len(lines)):
    msg = lines[i]
    w, h = font.getsize(msg)
    x = 0
    y = i * h
    draw.text((x, y), msg, inky_display.BLACK, font)

inky_display.set_image(img)
inky_display.show()
