# reddit-flair-bot

Python script for 'old' reddit for handling PMs with a view to assigning user flair (image or image/text) based on their content. The main use case for this is for subreddits who want to allow their users to choose from more than 350 flairs (this is the current limit for flair templates in subreddits).

# Requirements

Requires [Python](https://www.python.org/downloads/) (2.7, and 3.3-3.8 supported) and [PRAW](https://github.com/praw-dev/praw) to work.

It also requires you to [set up](https://github.com/reddit/reddit/wiki/OAuth2) either a script or web app so you can authorise the bot to read PMs, mark PMs as read, and apply flair to users. Whichever you choose, the credentials will need to be entered into the [conf.ini](https://github.com/gavin19/reddit-flair-bot/blob/master/conf.ini) file.

# Info

As it stands, this is the current script used in /r/football to handle the ~700 possible flairs. The PMs originate from users via /r/FootballBot. You will need to make your own sub (or preferably a wiki page in your subreddit) and populate it with links that point to a preset PM. An example link for a PM would be

    [Cat](http://www.reddit.com/message/compose/?to=the_bot_account&subject=flair&message=cat)

where the subject is set to `flair` (can be changed in the conf.ini file) and the body of the message would be `cat`. The user then sends this PM and the recipient account (whichever account you choose to run the bot through) acts on the content of it.

You need to add at least a list of the class names of your flairs to the `flair_list.csv` file. A sample file is provided, with the contents

    cat,Garfield
    dog,Scooby
    parrot
    shark

The format of each line must be `class_name` or `class_name,optional default text`. As you can see, you can have some flairs with default text and some without. Based on the example PM link above, the user would have a flair with a class name of `cat` applied, in addition to text of `Garfield`.

Unlike flairs that can be selected in the subreddit, the user can't edit/remove text. You can still allow users to add their own text if so desired. You will need to detail this in the subreddit/wiki page. For them to do this, they'll need to add this text directly after the class name. An example PM would be

https://www.reddit.com/message/compose/?to=the_bot_account&subject=flair&message=cat,custom%20text%20here

# Configuration

The configuration file (`conf.ini`) has six sections.

#### [app]

The `app_id` and `app_secret` values can be found after you've created your reddit script/web app.

The `user_agent` is what identifies the bot when connecting to reddit. Defaults to `Flair updater`, but you should change it to something like `Flair updater for /r/somesub`.

The `auth_type` will be whichever app type you chose to use. Must be either `script` (default) or `webapp`.

#### [auth-script]

Applicable only if you're using a script-type app.

The username and password of the account that you're going to use for the bot.

#### [auth-webapp]

Applicable only if you're using a web-type app.

The `token` value must be a valid refresh token. See [here](https://praw.readthedocs.io/en/latest/getting_started/authentication.html#web-application) to acquire the auth URL. Note, you require the `privatemessages` and `modflair` scopes. Once you've done that, go [here](https://praw.readthedocs.io/en/latest/getting_started/authentication.html#using-refresh-token) to find out how to get the token.

#### [subreddit]

The name of the subreddit you're targeting.

#### [subject]

The subject that you used in the PM links. This is so the bot can identify PMs that are intended for it rather than general PMs that the account may receive. Defaults to `flair`.

#### [log]

If you want the bot to keep a record of applied flairs (with timestamp). Defaults to `True`. Change to `False` if you want to disable logging.

# Finally

Once everything is in place, to run, execute

    python flair_bot.py

from a terminal/command prompt or schedule it to run intermittenly with cron/task scheduler.

# Support

PM [/u/gavin19](https://www.reddit.com/message/compose/?to=gavin19&subject=flair%20bot) on reddit.
