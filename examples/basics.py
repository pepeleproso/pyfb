#!/usr/bin/env python
from pyfb import Pyfb

#Your APP ID. It Needs to register your application on facebook
#http://developers.facebook.com/
FACEBOOK_APP_ID = '178358228892649'

facebook = Pyfb(FACEBOOK_APP_ID)

#Opens a new browser tab instance and authenticates with the facebook API
#It redirects to an url like http://www.facebook.com/connect/login_success.html#access_token=[access_token]&expires_in=0
facebook.authenticate()

#Copy the [access_token] and enter it below
token = raw_input("Enter the access_token\n")

#Sets the authentication token
facebook.set_access_token(token)

#Gets info about myself
me = facebook.get_myself()

print "-" * 40
print "Name: %s" % me.name
print "From: %s" % me.hometown.name
print

print "Speaks:"
for language in me.languages:
    print "- %s" % language.name

print
print "Worked at:"
for work in me.work:
    print "- %s" % work.employer.name

print "-" * 40

#Customizing operations using params
#See https://developers.facebook.com/docs/reference/api/ for a complete list of params
#Gets status about myself
params = {}

#Parameters that enable you to filter and page through data (limit, offset)
params["limit"] = 1
params["offset"] = 1

#You can restrict the fields returned in a search using the fields parameter
params["fields"] = "message"
message = facebook.get_statuses("me", params)[0].message
print message
