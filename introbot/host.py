# ======================================================================

import numpy
import csv
import string

# ======================================================================

class Host(object):
    """
    NAME
        Host

    PURPOSE
        Define a servant who can introduce people via Twitter, given 
        some basic information about them.

    COMMENTS
        The Host listens to a database in csv format. 

    INITIALISATION
    
    METHODS

       listen(database)
       
       introduce(twitter)

    BUGS

    AUTHORS
      This file is part of the IntroBot project, distributed under the
      GPL v2, by David Harris and Phil Marshall
    """

# ----------------------------------------------------------------------------

    def __init__(self):
        
        self.name = 'a host, who will be making the introductions'
        self.keywords = []
        self.tweets = []
        
        return None

# ----------------------------------------------------------------------------

    def __str__(self):
        return 'I am %s' % (self.name)

# ----------------------------------------------------------------------------

    def listen(self,database):
        
        # Read in a csv database:
        
        self.users = []
        self.bios = []

        db = csv.reader(open(database,"rb"))
        for row in db:    
            self.users.append(row[0])
            self.bios.append(row[1])
        
        # Check inputs:
        
        print "IntroBot: heard about ",len(self.users)," people: ",self.users
        
        for k in range(len(self.users)):
            print "IntroBot: knows that "+self.users[k]+" once said, ",self.bios[k]
        
        # Make a set of keywords:
        
        self.get_keywords()
                
        return None

# Notes:

# # One day we might want to read twitter to find users that should be introduced...
# x = t.search.tweets(q="#KIPAC10")
# print x


# ----------------------------------------------------------------------------

    def get_keywords(self):
        
        # Count words:
        
        count = dict()
        for bio in self.bios:
            
            for word in bio.split(' '):
            
                word = word.strip(string.punctuation + string.whitespace)
                word = word.lower()
                if len(word) > 0: count[word] = count.get(word,0) + 1
            
        # Find frequently occurring words:
        
        buzzwords = []
        for word in count:
            if count[word] >= 2 and count[word] < 6:
                buzzwords.append(word)
        
        # Reject commonly used words:
        
        commonwords = ['the','of','and','a','to','in','is','you','that','it','he','was','for','on','are','as','with','his','they','I','at','be','this','have','from','or','one','had','by','word','but','not','what','all','were','we','when','your','can','said','there','use','an','each','which','she','do','how','their','if','will','up','other','about','out','many','then','them','these','so','some','her','would','make','like','him','into','time','has','look']
        for word in buzzwords:
            if word not in commonwords:
                self.keywords.append(word)

        # Report:
        
        print "IntroBot: noticed keywords ",self.keywords
        
        return None
        
# ----------------------------------------------------------------------------

    def introduce(self,t):
        
        # Pair people up based on keywords:
        
        self.make_matches()
        
        # Loop through pairings, making introductions!
        
        for tweet in self.tweets:
            
            print "Introbot: making the following introduction:"
            print "  ",tweet
            # t.statuses.update(status=tweet)
        
        return

# ----------------------------------------------------------------------------

    def make_matches(self):

        # Loop over keywords, finding people who mentioned them:
        
        for word in self.keywords:
            
            people = ''
            count = 0
            for k in range(len(self.users)):
                if word in self.bios[k]:
                     people = people + ' '+self.users[k]
                     count += 1
            
            if count == 2:
                ALL = 'both'
            else:
                ALL = 'all'
            self.tweets.append("Hey"+people+", you "+ALL+" like #"+word)
        
        return None
        
#=============================================================================
