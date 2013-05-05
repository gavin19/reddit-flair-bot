reddit-flair-bot
================

Simple Python script for handling incoming PMs with a view to assigning flair based on their content.

Requires PRAW to run (and Python of course).

As it stands, this is the current script used in /r/football to handle the near 700 possible flairs. The PMs originate from users via /r/FootballBot and are autofilled to match the

    'prefixed_country_name-abbreviated_team_name' : 'full_team_name'
    
as seen in the list of teams. The team name is the text injected into the flair, so it assigns both an image and text.

