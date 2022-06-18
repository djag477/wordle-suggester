# Tweepy documentation --> https://docs.tweepy.org/en/stable/api.html#tweepy.API.update_status

import tweepy
import random as r

# Variables
#Find your keys and tokens among your Twitter app settings

consumer_key = "" 
consumer_secret = "" 
access_token = "" 
access_token_secret = ""

with open("words.txt") as f:
   word_list = f.read().splitlines()

clean_list = [x for x in word_list if len(x) == 5 and x.isalpha() and x[0] != x[0].capitalize()]

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)


#Functions
def random_word():
   day_word = clean_list[r.randint(0, len(clean_list) + 1)]   
   return f"{day_word.upper()}  #wordle"

def tweet():
   api.update_status(status = random_word())

tweet()
