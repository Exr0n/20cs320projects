# from https://towardsdatascience.com/how-to-scrape-tweets-from-twitter-59287e20f0f1
import GetOldTweets3 as got
import datetime

text_query = 'technology'
count = 1000

# Creation of query object
tweetCriteria = got.manager.TweetCriteria().\
    setQuerySearch(text_query).\
    setMaxTweets(count)
# Creation of list that contains all tweets
print("getting tweets")
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
print("got tweets!")

with open(f"scrapes/tweets_{datetime.date.today()}.txt", "a+") as wf:
    for tweet in tweets:
        wf.write(tweet.text + '\n')
