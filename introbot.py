from twitter import *

print "Hello, World!"

t = Twitter(auth=OAuth("1873916461-IRdIhbpjeQdsPufbZK4dX7l9SUMoncAUBxYDZpn", "Jhgy1Yy0jNueJgmmp21eBQl8k0FYdmxHdTN7TUvBw", "oH4bcjSIjvHVQDRQT8hYw", "td1U71THL4Ubnj8NYCpg1U85d0KaLvslfXSoehFORs"))

print "Twitter object set up"

#t.search.tweets(q="#pycon")

#s = t.statuses.home_timeline()

t.statuses.update(status="Hello world!")

#t.direct_messages.new(
#    user="physicsdavid",
#    text="Test python tweet")

