# imports
import praw
from time import gmtime, strftime

# main function


def main():
    teams = {
        'team-gb': 'Team GB 2012',
        'misc-1966-england': 'World Cup - England \'66',
        'misc-1970-mexico': 'World Cup - Mexico \'70',
        'misc-1974-wgermany': 'World Cup - West Germany \'74',
        'misc-1978-holland': 'World Cup - Holland \'78',
        'misc-1982-spain': 'World Cup - Spain \'82',
        'misc-1986-mexico': 'World Cup - Mexico \'86',
        'misc-1990-italy': 'World Cup - Italy \'90',
        'misc-1994-usa': 'World Cup - USA \'94',
        'misc-1998-france': 'World Cup - France \'98',
        'misc-2002-japan': 'World Cup - Japan 2002',
        'misc-2006-germany': 'World Cup - Germany 2006',
        'misc-2010-south-africa': 'World Cup - S.Africa 2010',
        'misc-2014-rio': 'World Cup - Rio 2014',
        'misc-2014-rio2': 'Rio 2014 Logo',
        'misc-bundes': 'Bundesliga',
        'misc-chmpl': 'Champions League',
        'misc-faprem': 'FA Premier League',
        'misc-seriea': 'Serie A',
        'misc-wil': 'FC Wil',
        'misc-pahang': 'Pahang FA',
        'misc-fcman': 'FC United of Manchester',
        'misc-afctel': 'AFC Telford'
    }
    print "Fired: " + strftime("%Y-%m-%d %H:%M:%S", gmtime())
    r = praw.Reddit(user_agent='Some bot name for some subreddit')
    r.login('some_user_name', 'some_password')
    for msg in r.get_unread(limit=None):
        subj = str(msg.subject)
        print "Subject: " + subj
        if subj == 'crest':
            print msg
            auth = str(msg.author)
            body = str(msg.body)
            print "Author: " + auth
            print "Message content: " + body
            sub = r.get_subreddit('football')
            if body in teams:
                ftext = str(teams[body])
                sub.set_flair(auth, ftext, body)
                with open('log.txt', 'a') as logfile:
                    tn = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    lm = ' : ' + body + ' @ ' + tn
                    logfile.write('\n\rAdded: ' + auth + ' : ' + ftext + lm)
                print "Setting flair: " + auth + " : " + ftext + " : " + body
                msg.mark_as_read()

if __name__ == '__main__':
    main()
