# BrainStation Capstone

## Obtaining Twitter Data
I used the STREAM API

## Processing Twitter Data
The tokenizer comes from the ARK NLP Project (https://github.com/myleott/ark-twokenize-py). I forked the project and made modifications. I simply copied the file here to avoid dealing with git's submodules.
I added an emoji regex, from the emoji module (https://github.com/carpedm20/emoji) to the tokenizer so I could treat emojis as their own entities. The emoji module has a complete regex that is constructed from the unicode consortium's website (http://www.http://unicode.org/emoji/charts/emoji-list.html). 
The desired output is just the tweet text without any fuzz (AtMentions,URLs, ReTweets, ...). This data is enhanced by identifying the emojis in the tweet, the number of tokens and number of emojis.

Sample line from the csv:
[tweet_text, emojis, n_tokens, n_emojis]
