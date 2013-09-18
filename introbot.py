import introbot

# Connect to twitter, using your own account...

try: from introbot import connection
except:
    print "IntroBot: unable to connect to to Twitter"
    sys.exit()

print "IntroBot: connected to Twitter: ",connection.line

# Instantiate a host, who will do the introductions:

jeeves = introbot.Host()

# Pass it the data it needs to figure out what to say:

# database = 'example/SHD_users_bios.csv'
database = 'example/pie.csv'
jeeves.listen(database)

# Pass the twitter object to the IntroBot, and have it start sending statuses.

jeeves.introduce(connection.line)

# Done!
