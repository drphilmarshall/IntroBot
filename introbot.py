from twitter import *
import introbot

# Connect to twitter, using the @SHDIntroBot account...

t = Twitter(auth=OAuth("1873916461-IRdIhbpjeQdsPufbZK4dX7l9SUMoncAUBxYDZpn", "Jhgy1Yy0jNueJgmmp21eBQl8k0FYdmxHdTN7TUvBw", "oH4bcjSIjvHVQDRQT8hYw", "td1U71THL4Ubnj8NYCpg1U85d0KaLvslfXSoehFORs"))

print "IntroBot: connected to Twitter"

# Instantiate a host, who will do the introductions:

jeeves = introbot.Host()

# Pass it the data it needs to figure out what to say:

database = 'example/SHD_users_bios.csv'
jeeves.listen(database)

# Pass the twitter object to the IntroBot, and have it start sending statuses.

jeeves.introduce(t)

# Done!
