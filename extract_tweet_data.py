#!/usr/bin/env python3

import json
import argparse
import twokenize

import regex
import sys
import pandas as pd


def get_argparser():
    parser = argparse.ArgumentParser(description="This script extracts the text and emojis out of a Tweet. This script expects as input the stream.json file obtained from the Twitter API (See twitter_stream_download.py. It outputs a csv file of the tweet text, the emojis in the tweet, the number of tokens in the text, and the number of emojis in the tweet.")
    parser.add_argument("-i",
                        "--infile",
                        dest="infile",
                        help="Path of file containing the raw tweets")
    parser.add_argument("-o",
                        "--outfile",
                        dest="outfile",
                        help="Path of output csv",
                        default="output.csv")

    return parser

url_re = regex.compile(twokenize.url)
punctSeq_re = regex.compile(twokenize.punctSeq)
emoji_re = regex.compile(twokenize.Emoji)
Hashtag_re = regex.compile(twokenize.Hashtag)
AtMention_re = regex.compile(twokenize.AtMention)


def filter_tokens_emojis(tokens):
    filtered_tokens = []
    emojis = []
    for i in tokens:
        if url_re.match(i):
            pass
            #print("URL skipped:", i)
        elif punctSeq_re.match(i):
            pass
            #print("Punct skipped:", i)
        elif AtMention_re.match(i):
            pass
            #print("AtMention skipped:", i)
        elif Hashtag_re.match(i):
            pass
            #print("Hashtag modified:", i)
            #Remove the # from the hashtag
            filtered_tokens.append(i[1:])
        elif emoji_re.match(i):
            filtered_tokens.append(i)
            emojis.append(i)
        else:
            pass
            filtered_tokens.append(i)
    return filtered_tokens, emojis
 

if __name__ == '__main__':
    parser = get_argparser()
    args = parser.parse_args()
    with open(args.infile) as infile:
        line_n = 0 #line counter to report where error occurs
        output_data = []
        for line in infile:
            line_n += 1
            raw_data = ""
            try:
                raw_data = json.loads(line)
            except:
                print(sys.exc_info()[0])
                print(sys.exc_info()[1])
                #Offending line number and contents are printed
                #Sometimes the character cannot be recognized so I remove the line if needed
                print(line_n)
                print(line)
            if 'limit' in raw_data:
                continue
            if 'retweeted_status' in raw_data:
                continue
            tokens = twokenize.tokenizeRawTweetText(raw_data['text'])
            filtered_tokens, emojis = filter_tokens_emojis(tokens)
            output_data.append([" ".join(filtered_tokens), " ".join(emojis),
                len(filtered_tokens), len(emojis)])

    df = pd.DataFrame(output_data, columns=['tweet_text', 'emojis', 'n_tokens', 'n_emojis'])
    df.to_csv(args.outfile)
