#!/usr/bin/env python3
import praw
import OAuth2Util
import sys
import os
from time import gmtime, strftime
try:
    from flair_list import flairs
except ImportError as e:
    print("Flairs file can't be accessed\n")
    print(e)
    sys.exit()
except SyntaxError as e:
    print("There is a syntax error in the flair list\n")
    print(e)
    sys.exit()

"""

Starting August 2015 reddit will require all logins to be made through OAuth. 
In order to log in through OAuth you'll need to follow a few simple steps 
(see https://github.com/SmBe19/praw-OAuth2Util/blob/master/OAuth2Util/README.md#reddit-config)

The first time you run the script a browser will open and you'll have to log into the account to authorize the app, 
if you don't do this the script will not write any tokens and it simply won't work. Message 
/u/zzqw- if you need help with this.

OAuth changes made by /u/zzqw- + /u/GoldenSights
OAUth2Util.py by /u/SmBe19 (https://github.com/SmBe19/praw-OAuth2Util)

"""


class FlairBot:

    # User blacklist
    BLACKLIST = ['sampleuser', 'sampleUSER2']

    # Set a descriptive user agent to avoid getting banned.
    # Do not use the word `bot' in your user agent.
    r = praw.Reddit(user_agent="Flair changer for /r/subreddithere")

    o = OAuth2Util.OAuth2Util(r)

    """ The SUBJECT will be the default subject of your PMs
    when you create the URLs, eg.

    reddit.com/message/compose/?to=some_user&subject=flair&message=some_message

    PMs require a subject, but it's also a simple way of identifying
    PMs that are directed towards the flairs and not just a general PM"""
    SUBJECT = 'flair'

    # TARGET_SUB is the name of the subreddit without the leading /r/
    TARGET_SUB = 'yoursubreddithere'

    # Turn on output to log file in current directory - log.txt
    LOGGING = True

    # Class variable to hold the unread pms
    pms = None

    def init(self):
        if self.LOGGING:
            os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.login()


    def login(self):
        try:
            self.o.refresh()  # Refresh the OAuth token, only valid for 1hr
            self.fetch_pms()
        except:
            raise


    def fetch_pms(self):
        """ Get a listing of all unread PMs for the user account """
        self.pms = self.r.get_unread(limit=None)
        if self.pms is not None:
            self.process_pms()

    def process_pms(self):
        for pm in self.pms:
            if str(pm.subject) == self.SUBJECT:
                author = str(pm.author)  # Author of the PM
                if author.lower() in (user.lower() for user in self.BLACKLIST):
                    continue
                content = str(pm.body)  # Content of the PM
                subreddit = self.r.get_subreddit(self.TARGET_SUB)
                if content in flairs:
                    # Get the flair text that corresponds with the class name
                    flair_text = str(flairs[content])
                    subreddit.set_flair(author, flair_text, content)
                    if self.LOGGING:
                        self.log(author, content, flair_text)
                pm.mark_as_read()  # Mark processed PM as read
        sys.exit()

    def log(self, author, content, flair_text):
        with open('log.txt', 'a', encoding='utf-8') as logfile:
            time_now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            log_text = 'Added: ' + author + ' : ' \
                + flair_text + ' : ' \
                + content + ' @ ' + time_now + '\n'
            logfile.write(log_text)

FlairBot().init()
