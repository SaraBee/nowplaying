from radio import Radio

track = Radio.fetch_track()
composer = Radio.get_composer(track)
title = Radio.get_title(track)

guess_composer = input("Who do you think the composer is? Guess: ")

composer_toks = composer.split(" ")
composer_last_tok = composer_toks.pop()

if guess_composer == composer or guess_composer == composer_last_tok:
    print("Correct! The piece is " + title + " by " + composer)
else:
    second_guess = input("Hm, that wasn't right. Try again: ")
    if second_guess == composer or second_guess == composer_last_tok:
        print("Correct! The piece is " + title + " by " + composer)
    else:
        print("Whoops! The piece is " + title + " by " + composer)
