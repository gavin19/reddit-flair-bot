reddit-flair-bot
================

Simple Python script for handling incoming PMs with a view to assigning flair based on their content.

Requires PRAW to run (and Python of course).

As it stands, this is the current script used in /r/football to handle the near 700 possible flairs. The PMs originate from users via /r/FootballBot and are autofilled to match the

    'flair_shortcode' : 'flair_text'
    
as seen in the list of teams (flair_list.py). The team name is the text injected into the flair, so it assigns both an image and text. A typical prefilled PM would might look like

    http://www.reddit.com/message/compose/?to=RFootballBot&subject=crest&message=eng-fcman

where the subject is set to 'crest' (can be changed in the script) and the body of the message would be `eng-fcman`.

A (truncated) list of teams is included as an example of how your flair list should be structured. For example

    flairs {
        'eng-fcman': 'FC United of Manchester',
        'eng-afctel': 'AFC Telford',
        'eng-chester': 'Chester F.C',
        'eng-arsenal': 'Arsenal',
        'eng-aston-villa': 'Aston Villa'
    }

where `eng-fcman` would be the text contained in the PM and also the string used as the class name in the CSS. `FC United of Manchester` being the text applied to the flair. In your stylesheet you'd have something like

    .flair {
        background: url(%%spritesheet%%) no-repeat -9999px -9999px;
        text-indent: -9999px;
        height: 20px;
        line-height: 20px;
        min-width: 20px;
        text-indent: 23px;
    }
    .flair-eng-fcman { background-position: 0 0; }

To run, execute

    python flair_bot.py

from the terminal/cmd or schedule it to run intermittenly with cron/task scheduler.

