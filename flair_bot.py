#! /usr/bin/env python

import praw
import sys
from time import gmtime, strftime
try:
    from flair_list import flairs
except ImportError as e:
    print("Flairs file can't be accessed")
    print(e)
    sys.exit()
except SyntaxError as e:
    print("There is a syntax error in the flair list\n")
    print(e)
    sys.exit()

UA = '/u/some_user flair bot for /r/some_subreddit'
USER_NAME = 'user_name'
PASSWD = 'password'
# The SUBJECT will be the default subject of your PMs
# when you create the URLs. PMs require a subject
# but it's also a simple way of identifying
# PMs that are directed towards the flairs
# and not just a general PM
SUBJECT = 'crest'
# TARGET_SUB is to be the name of the subreddit
# without the leading /r/
TARGET_SUB = 'example_subreddit'

def main():
    print "Fired: " + strftime("%Y-%m-%d %H:%M:%S", gmtime())
    r = praw.Reddit(user_agent=UA)
    r.login(USER_NAME, PASSWD)
    for msg in r.get_unread(limit=None):
        subj = str(msg.subject)
        print "Subject: " + subj
        if subj == SUBJECT:
            print msg
            auth = str(msg.author)
            body = str(msg.body)
            print "Author: " + auth
            print "Message content: " + body
            sub = r.get_subreddit(TARGET_SUB)
            if body in flairs:
                ftext = str(flairs[body])
                sub.set_flair(auth, ftext, body)
                with open('log.txt', 'a') as logfile:
                    tn = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    lm = ' : ' + body + ' @ ' + tn
                    logfile.write('\n\rAdded: ' + auth + ' : ' + ftext + lm)
                print "Setting flair: " + auth + " : " + ftext + " : " + body
                msg.mark_as_read()

if __name__ == '__main__':
    main()
