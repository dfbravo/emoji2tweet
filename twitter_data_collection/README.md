#Collecting and Preprocessing Twitter Data

## Downloading Tweets
I used the tweepy module to interface with the Twitter Stream API. The result are json files, one for each attempt to download, which contain all the data obtained from the Twitter API. Below I extract the tweet text and ignore the metadata.

```
usage: twitter_stream_download.py [-h] [--id INDEX] [-o DATA_DIR] [-r]
                                  [-l LIMIT] [-n NAME]

This script downloads tweets within a bounding box. An output folder is required. The tweets are stored in a file per attempt. You can set the script to attempt when errors occur. The filename convention is stream_<label><id>.json

optional arguments:
  -h, --help            show this help message and exit
  --id INDEX            Integer used to differentiate files. Appended at the
                        end of the filename. stream_<label><id>.json
  -o DATA_DIR, --outut-dir DATA_DIR
                        Output/Data Directory
  -r, --retry           Retry on error. Sometimes the connection is lost.
  -l LIMIT, --limit LIMIT
                        Number of retry attempts
  -n NAME, --name NAME  Label used to differentiate files
                        stream_<label><id>.json
```


The credentials required are obtained by creating a Twitter Developer account. The credentials are expected in a file called `twitter_stream_config.py`
```
consumer_key=
consumer_secret=
access_token=
access_secret=
```

## Extracting Tweet Text and Tokenizing
The resulting json file contains a lot of metadata that is not required for this project. I read the resulting json line-by-line and keep only the tweet text. Retweets are ignored.

The tokenizer used is obtained from the ARK-Tweet-NLP project. I forked the python port from here: https://github.com/myleott/ark-twokenize-py. I did not include the fork as a submodule to avoid extra work.

The tokenizer was adapted for emojis. The emoji module is used to obtained a rege pattern that properly tokenizes emojis. 

Tokenizing emojis is difficult since they can be variable in size. To avoid this, one could create an exhaustive list of all the emojis available. That's essentially what is done here.

Additionally, AtMentions and URLs are ignored by the tokenizer Hashtags are stripped of the '#' as they are sometimes single words which I believe is relevant data.

The output is a csv file that contains the tweet text, emojis, and their counts.

```
usage: extract_tweet_data.py [-h] [-i INFILE] [-o OUTFILE]

This script extracts the text and emojis out of a Tweet. This script expects
as input the stream.json file obtained from the Twitter API (See
twitter_stream_download.py. It outputs a csv file of the tweet text, the
emojis in the tweet, the number of tokens in the text, and the number of
emojis in the tweet.

optional arguments:
  -h, --help            show this help message and exit
  -i INFILE, --infile INFILE
                        Path of file containing the raw tweets
  -o OUTFILE, --outfile OUTFILE
                        Path of output csv
```
