# Now Playing
Some scripts and stuff that work with data from NYC classical radio station WQXR. Read more about this project [over on my blog](http://sarabee.github.io/2020/09/13/is-this-mahler/).

<img src="https://raw.githubusercontent.com/SaraBee/SaraBee.github.io/master/images/whatnow-closeup.jpg" width="400"/>

## tmux status bar widget
To add now playing information to your tmux status bar, add the following to your `.tmux.conf`:

`set -g status-right #(python3 path/to/nowplaying/tmux.py)`

I added some color and a clock to mine:

`set -g status-right '#[bg=#d7ff5f] #(python3 /path/to/nowplaying/tmux.py)  |  [%H:%M] '`

## An e-paper display
Written for Pimoroni's [inky](https://github.com/pimoroni/inky) e-ink displays, using autodetection to work with both the inkypHAT and larger inkywHAT. If you've got a Raspberry Pi and inky dispplay, you can run `whatnow.py` on a cron (mine runs once a minute) to create your very own WQXR announcer display.

## A Guess the Composer game
To play, clone this repo, turn on WQXR (or listen to their
livestream and don't peek at what's currently on) and run `guess.py` however
you run python3 scripts.
