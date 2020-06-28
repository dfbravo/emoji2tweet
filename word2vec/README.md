# Training the Word2Vec Model

The word2vec.py script trains a word2vec model using the gensim library. The input data is all the tweets joined by a space in a single line. The reason being that I followed the process from my previous project (wordmoji2vec). 

To flatten the tweets use `flatten_tweets.py`
```
usage: flatten_tweets.py [-h] -i INFILE [-o OUTFILE]

This script will convert a csv file containing tweet text and flatten it into
a single line. The input is expected to be a csv file where a column
'tweet_text' contains the text to be flattened. Please look at the EDA
notebook to create this csv file.

optional arguments:
  -h, --help  show this help message and exit
  -i INFILE   Path to input csv with a column 'tweet_text'
  -o OUTFILE  Path to output file with all the tweets joined by a space into
              one line
```

To train the model use the script `word2vec.py`
```
usage: word2vec.py [-h] -i INFILE [-o OUTFILE]

This script trains a word2vec model on an input dataset. The input is expected
to all be in one line. Please use flatten_tweets.py to do so. The output is
the w2v.model.

optional arguments:
  -h, --help  show this help message and exit
  -i INFILE   Path to input file containing all the tweets in one line
  -o OUTFILE  Path to output file containing the w2v model
```
