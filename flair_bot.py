""" Flair bot. """
import sys
import os
import csv
from configparser import ConfigParser
from time import gmtime, strftime
import praw

class FlairBot:
    """ Flair bot. """

    subject = None
    logging = True
    conf = None
    reddit = None
    flairs = {}

    def __init__(self):
        """ Read config file. """

        conf = ConfigParser()

        if os.path.exists('conf.ini'):
            self.conf = conf.read('conf.ini')
        else:
            raise FileNotFoundError('The config file, conf.ini, was not found.')

        if self.conf.get('log', 'logging') == 'True':
            os.chdir(os.path.dirname(os.path.abspath(__file__)))
        else:
            self.logging = False

        self.login()

    def login(self):
        """ Log in via script/web app. """

        app_id = self.conf.get('app', 'app_id')
        app_secret = self.conf.get('app', 'app_secret')
        user_agent = self.conf.get('app', 'user_agent')

        if self.conf.get('app', 'auth_type') == 'webapp':
            token = self.conf.get('auth-webapp', 'token')
            self.reddit = praw.Reddit(client_id=app_id,\
                            client_secret=app_secret,\
                            refresh_token=token,\
                            user_agent=user_agent)
        else:
            username = self.conf.get('auth-script', 'username')
            password = self.conf.get('auth-script', 'passwd')
            self.reddit = praw.Reddit(client_id=app_id,\
                            client_secret=app_secret,\
                            username=username,\
                            password=password,\
                            user_agent=user_agent)

        self.get_flairs()

    def get_flairs(self):
        """ Read flairs from CSV. """

        with open('flair_list.csv') as csvf:
            csvf = csv.reader(csvf)
            flairs = {}
            for row in csvf:
                if len(row) == 2:
                    flairs[row[0]] = row[1]
                else:
                    flairs[row[0]] = None

        self.flairs = flairs
        self.fetch_pms()

    def fetch_pms(self):
        """ Grab unread PMs. """

        target_sub = self.conf.get('subreddit', 'name')
        subject = self.conf.get('subject', 'subject')
        for msg in self.reddit.inbox.unread():
            if msg.subject == subject:
                self.process_pm(msg, target_sub)
        sys.exit()

    def process_pm(self, msg, target_sub):
        """ Process unread PM. """

        author = msg.author
        content = msg.body.split(',', 1)
        class_name = content[0].rstrip()
        subreddit = self.reddit.subreddit(target_sub)

        if class_name in self.flairs:
            if len(content) > 1:
                flair_text = content[1].lstrip()[:64]
            else:
                flair_text = self.flairs[class_name] or ''

            subreddit.flair.set(author, flair_text, class_name)
            if self.logging:
                self.log(author, flair_text, class_name)

        msg.mark_read()

    @staticmethod
    def log(user, text, cls):
        """ Log applied flairs to file. """

        with open('log.txt', 'a', encoding='utf-8') as logfile:
            time_now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            log = 'user: ' + user
            log += ' | class(es): ' + cls
            if len(text):
                log += ' | text: ' + text
            log += ' @ ' + time_now + '\n'
            logfile.write(log)

FlairBot()
