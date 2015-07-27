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
The first time you run the script a browser will open and you'll have to log into the account and authorize the app, if you don't do this the script will not write any tokens and it simply won't work. Message /u/straightouttasweden if you need help with this step.

OAuth changes made by /u/straightouttasweden + /u/GoldenSights

OAuth2Util.py + OAuth guide by /u/SmBe19 (https://github.com/SmBe19/praw-OAuth2Util)

Utility that allows for easier handling of OAuth2 with PRAW.

In your code you can use it like this:

	import praw
	import OAuth2Util

	r = praw.Reddit("Useragent")
	o = OAuth2Util.OAuth2Util(r)

That's it! To refresh the token (it is only valid for one hour), use `o.refresh()`. This checks first whether the token is still valid and doesn't request a new one if it is still valid. So you can call this method befor every block of PRAW usage. Example:

	import time
	while True:
		o.refresh()
		print(r.get_me().comment_karma)
		time.sleep(3600)

If you want to have different tokens (e.g if your script has to log in with different users), you have to specify at least a different oauthtoken config file.

## Reddit Config
In order to use OAuth2, you have to create an App on Reddit (https://www.reddit.com/prefs/apps/). For most use cases you will choose `script` as app type. You have to set the `redirect uri` to `http://127.0.0.1:65010/authorize_callback`, the other fields are up to you.

## Config
OAuth2Util uses one config file to store the information. Before you can use it, the first two must be filled out manually by you, the third one will automatically be filled out when you authorize the script. Your `oauth.txt` should contain these lines:
	
	# Config 
	scope=identity,account,edit,flair,history,livemanage,modconfig,modflair,modlog,modothers,modposts,modself,modwiki,mysubreddits,privatemessages,read,report,save,submit,subscribe,vote,wikiedit,wikiread # These grant the bot to every scope, only use those you want it to access.
	refreshable=True

	# Appinfo
	app_key=thisistheid
	app_secret=ThisIsTheSecretDoNotShare

	# Token
	token=None
	refresh_token=None

##LICENSE

The MIT License (MIT)

Copyright (c) 2015 Gavin McAlister

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
