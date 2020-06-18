# THIS SCRIPT HAS BEEN MODIFIED. dfbravo Nov 15, 2016. ORIGINAL in the link
# Source: https://gist.github.com/bonzanini/af0463b927433c73784d#file-twitter_stream_download-py

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
import string
import twitter_stream_config
import json

import sys
import traceback

def get_parser():
    """Get parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Twitter Downloader")
    parser.add_argument("-i",
                        "--id",
                        dest="index",
                        type=int,
                        help="Index of file name")
    parser.add_argument("-d",
                        "--data-dir",
                        dest="data_dir",
                        help="Output/Data Directory")
    parser.add_argument("-r",
                        "--restart",
                        dest="restart",
                        help="Restart on error",
                        action="store_true")
    parser.add_argument("-l",
                        "--limit",
                        dest="limit",
                        help="Limit repeats",
                        type=int)
    parser.add_argument("-n",
                        "--name",
                        dest="name",
                        help="Label used to differentiate files",
                        default="generic")
    return parser


class MyListener(StreamListener):
    """Custom StreamListener for streaming data."""

    def __init__(self, data_dir, label):
        fname = format_filename(label)
        self.outfile = "%s/stream_%s.json" % (data_dir, fname)

    def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                f.write(data)
                #print(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        print(status)
        return True


def format_filename(fname):
    """Convert file name into a safe string.

    Arguments:
        fname -- the file name to convert
    Return:
        String -- converted file name
    """
    return ''.join(convert_valid(one_char) for one_char in fname)


def convert_valid(one_char):
    """Convert a character into '_' if invalid.

    Arguments:
        one_char -- the char to convert
    Return:
        Character -- converted char
    """
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    if one_char in valid_chars:
        return one_char
    else:
        return '_'

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True,retry_count=3, retry_delay=5,retry_errors=set([401, 404, 500, 503]))

    i = args.index
    limit = args.limit + i
    while True:
        twitter_stream = Stream(auth, MyListener(args.data_dir, args.name + str(i)))
        try:
            #US
            twitter_stream.filter(locations=[-126.08,24.69,-64.91,49.67])

            #UK
            #twitter_stream.filter(locations=[-10.79,50.18,1.61,59.07])
        except KeyboardInterrupt:
            break
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print "Sleeping for 15min..."
            time.sleep(900)
            print "Done"

        if args.restart:
            i += 1
        else:
            break

        if i == limit:
            break

