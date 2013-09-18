try: from twitter import *
except:
    print "IntroBot: Twitter API is not installed."
    print "IntroBot: try 'pip install twitter' and re-run."
    sys.exit()

# Insert your account credentials here:

ConsumerKey = "";
ConsumerSecret = "";
AccessToken = "";
AccessTokenSecret = "";

# Connect to twitter:

line = Twitter(auth=OAuth(ConsumerKey,
                          ConsumerSecret,
                          AccessToken,
                          AccessTokenSecret))
