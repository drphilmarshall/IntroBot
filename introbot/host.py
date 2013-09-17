# ======================================================================

import numpy
import csv

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
        
        # Make a list of keywords:
        
        # self.make_keyword_list()
                
        return None

# Notes:

# # One day we might want to read twitter to find users that should be introduced...
# x = t.search.tweets(q="#KIPAC10")
# print x


# ----------------------------------------------------------------------------

    def introduce(self,t):
        
        # Pair people up based on keywords:
        
        # self.make_matches()
        
        # Loop through pairings, making introductions!
        
        # t.statuses.update(status="Hello world!")
        
        return

#=============================================================================
