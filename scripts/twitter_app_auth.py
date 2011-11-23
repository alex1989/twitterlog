#!/usr/bin/env python

import tweepy

CONSUMER_KEY = '6kTZIVPG6vQ3Io4dGSwA'
CONSUMER_SECRET = '0CdkAIH19oxe4vPA3ObeQwzi8mCNo4dr146SYoH9Cw'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url = auth.get_authorization_url()
print 'Please authorize: ' + auth_url
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)
print "ACCESS_KEY = '%s'" % auth.access_token.key
print "ACCESS_SECRET = '%s'" % auth.access_token.secret
