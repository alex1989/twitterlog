# -*- coding: utf-8 -*-

from logging import Handler, Formatter
import traceback
import re
import tweepy

_ws_re = re.compile(r'(\s+)(?u)')


class TwitterFormatter(Formatter):

    def __init__(self):
        Formatter.__init__(self, u'%(levelname)s: %(message)s')

    def formatException(self, exc_info):
        return ''.join(traceback.format_exception_only(*exc_info[:2])) \
                 .strip().decode('utf-8', 'replace')

    def format(self, record):
        rv = []
        length = 0
        for piece in _ws_re.split(Formatter.format(self, record)):
            length += len(piece)
            if length > 140:
                if length - len(piece) < 140:
                    rv.append(u'…')
                break
            rv.append(piece)
        return u''.join(rv)


class TwitterHandler(Handler):
    def __init__(self, consumer_key, consumer_secret, access_key, access_secret):
        super(TwitterHandler, self).__init__()
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        self.api = tweepy.API(auth)
        Handler.setFormatter(self, TwitterFormatter())

    def tweet(self, status):
        return self.api.update_status(status=status)

    def emit(self, record):
        try:
            msg = self.format(record)
            if isinstance(msg, str):
                msg = msg.encode('utf-8', 'replace')
            self.tweet(msg)
        except RuntimeError:
            pass
