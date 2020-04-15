# Now Playing
Some scripts and stuff that work with data from NYC classical radio station WQXR.

## tmux status bar widget
To add now playing information to your tmux status bar, add the following to your `.tmux.conf`:

`set -g status-right #(python3 path/to/nowplaying/tmux.py)`

I added some color and a clock to mine:

`set -g status-right '#[bg=#d7ff5f] #(python3 /path/to/nowplaying/tmux.py)  |  [%H:%M] '`

## A Guess the Composer game
To play, clone this repo, turn on WQXR (or listen to their
livestream and don't peek at what's currently on) and run `guess.py` however
you run python3 scripts.
