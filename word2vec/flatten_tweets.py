#!/usr/bin/python3

import argparse
import pandas as pd

def get_argparser():
    parser = argparse.ArgumentParser(description="This script will convert a csv file containing tweet text and flatten it into a single line. The input is expected to be a csv file where a column 'tweet_text' contains the text to be flattened. Please look at the EDA notebook to create this csv file.")
    parser.add_argument("-i", dest="infile", help="Path to input csv with a column 'tweet_text'", required=True)
    parser.add_argument("-o", dest="outfile",help="Path to output file with all the tweets joined by a space into one line", default="flat_tweets.txt")
    return parser

parser = get_argparser()
args = parser.parse_args()

infile=args.infile
outfile= args.outfile

with open(outfile, 'w', encoding='utf-8') as out_fp:
    df = pd.read_csv(infile)
    # Removing any rows that have NaN tweet text. That is an empty tweet.
    df_nona = df[df['tweet_text'].notna()]
    # join requires there are no NaN values
    tweets_one_line = ' '.join(df_nona['tweet_text'])
    out_fp.write(tweets_one_line)
