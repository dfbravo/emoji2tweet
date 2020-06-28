#!/usr/bin/python3

import gensim, logging
import argparse
import os
import sys
import pandas as pd

# logging for gensim
#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def get_argparser():
    parser = argparse.ArgumentParser(description="This script trains a word2vec model on an input dataset. The input is expected to all be in one line. Please use flatten_tweets.py to do so. The output is the w2v.model.")
    parser.add_argument("-i", dest="infile", help="Path to input file containing all the tweets in one line", required=True)
    parser.add_argument("-o", dest="outfile",help="Path to output file containing the w2v model", default="w2v.model")
    return parser

parser = get_argparser()
args = parser.parse_args()

infile=args.infile
outfile= args.outfile

# The choice for these parameters is mostly arbitrary. 
# I'm not evaluating the quality of these word2vec vectors, which is a flaw
# TODO: Evaluate word2vec vectors. Possibly use pretrained vectors
vector_size=300 # size of w2v vectors
min_count=5 # discard words that occur less than this threshold
n_threads=8 # num of threads for gensim
window_size=5 # size of window used for co-ocurrence
downsample_rate=1e-3 # downsampling of 
skipgram=1 # whether skipgram is used or not, 0 -> cbow
negative_samples=5 # num of negative samples used
n_train_iter=5 # num of training iterations

# Text8Corpus is a function created to specifically load the text8.zip dataset
# Which is a one-line textfile. Sentences are created from this one line
# Tweets are appended to each other to create one line
# This is an artifact of how I did my previous project
sentences = gensim.models.word2vec.Text8Corpus(infile)

# train word2vec model
model = gensim.models.Word2Vec(sentences, size=vector_size, min_count=min_count, workers=n_threads, window=window_size, sample=downsample_rate, sg=skipgram, negative=negative_samples, iter=n_train_iter)

# save the model
model.save(outfile)
