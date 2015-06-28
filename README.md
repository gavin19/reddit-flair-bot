reddit-flair-bot
================

Simple Python script for handling incoming PMs with a view to assigning flair based on their content, python 3 is needed for the bot to run.

Requires PRAW to run (and Python 3 of course).

As it stands, this is the current script used in /r/football to handle the near 700 possible flairs. The PMs originate from users via /r/FootballBot and are autofilled to match the

    'flair_shortcode' : 'flair_text'
    
as seen in the list of teams (flair_list.py). The team name is the text injected into the flair, so it assigns both an image and text. A typical prefilled PM might look like

    http://www.reddit.com/message/compose/?to=RFootballBot&subject=crest&message=eng-fcman

where the subject is set to 'crest' (can be changed in the script) and the body of the message would be `eng-fcman`.

A (truncated) list of teams is included as an example of how your flair list should be structured. For example

    flairs = {
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

    python3 flair_bot.py

from the terminal/cmd or schedule it to run intermittenly with cron/task scheduler.

#OAuth

Starting August 2015 reddit will require all logins to be made through OAuth. In order to log in through OAuth you'll need to follow a few simple steps.
The first time you run the script a browser will open and you'll have to log into the account and authorize the app, if you don't do this the script will not write any tokens and it simply won't work. Message /u/straigh$

OAuth changes made by /u/straightouttasweden + /u/GoldenSights
OAuth2Util.py + OAuth guide by /u/SmBe19 (https://github.com/SmBe19/praw-OAuth2Util)

## Reddit Config
In order to use OAuth2, you have to create an App on Reddit (https://www.reddit.com/prefs/apps/). For most use cases you will choose `script` as app type. You have to set the `redirect uri` to `http://127.0.0.1:65010/authorize_callback`, the other fields are up to you.

## Config
OAuth2Util uses three config files to store the information. You can specify the name of them when you create the Util. Before you can use it, you have to fill out the first two, the third one will be filled out.

### OAuthAppInfo
Contains the client id and client secret of the app.

	thisistheid
	ThisIsTheSecretDoNotShare

### OAuthConfig
Contains the requested scopes (separated by one `,`) and whether a refreshable token should be used.

	identity,read
	True

### OAuthToken
Contains the token and the refresh token. This config file is maintained by OAuth2Util, you don't have to do anything with it. If it shouldn't work anymore, just delete this file to request new tokens.

	VerySecretToken
	VerySecretRefreshToken
