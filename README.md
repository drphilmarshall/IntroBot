IntroBot
========

Introducing people who have common interests, on Twitter.

To make a whole lot of Twitter introductions at once, IntroBot just needs a plain text datafile listing your community's Twitter users, and some text describing their interests. IntroBot parses this text, pairs people up, and introduces them, gracefully. 

### Getting started

You'll need OAuth credentials to use the Twitter API -- once you have them, copy `introbot/connection_template.py` to `introbot/connection.py` and insert them. You then connect your own IntroBot to Twitter as follows:

    from introbot import connection

This makes a twitter object called `connection.line` which you can pass to your IntroBot host.

The example script, `introbot.py`, gives a simple example of how to use a csv datafile of users and interests to generate some introductory tweets. Here's what it does.

Instantiate a host, who will do the introductions:

    jeeves = introbot.Host()

Pass it the data it needs to figure out what to say:

    jeeves.listen('example/pie.csv')

Pass the twitter object to the IntroBot, and have it start sending statuses.

    jeeves.introduce(connection.line)
   
That's it! To actually send the tweets, just uncomment the statuses.update line in the `Host.introduce` method in `introbot/host.py`.


### Authors

* David Harris [@physicsdavid](http://twitter.com/physicsdavid)
* Phil Marshall [@drphilmarshall](http://twitter.com/drphilmarshall)

### License

GPL v2. Share and share alike!
