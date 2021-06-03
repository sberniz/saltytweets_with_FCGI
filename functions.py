import tweepy
import joblib
from os import getenv

# model imports for saltiness
model = joblib.load("models/tree_reg.pkl")
pipeline = joblib.load("models/sklearn_pipeline.pkl")
import tweepy
# twitter api keys
TWITTER_API_KEY= getenv('TWITTER_API_KEY')
TWITTER_API_SECRET_KEY= getenv('TWITTER_API_SECRET_KEY')


# #tweeter auth
TWITTER_AUTH = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
TWITTER = tweepy.API(TWITTER_AUTH,wait_on_rate_limit=True,)
#get trending


def get_trending():
  available = TWITTER.trends_place("23424977", exclude="hashtags")
  trending = {}
  for av in available[0]['trends']:
        if(av['tweet_volume'] != None):
              trending[av['name']] = av['tweet_volume']
  trending=sorted(trending.items(), key= lambda x:x[1], reverse=True)
  trends = [i[0] for i in trending]
  trends = trends[:10]      
  return trends

#get tweets

def get_tweets(trending):
  tweets_array = []
  for trend in trending:
    trend = str(trend)+" -filter:retweets"
    tweets = TWITTER.search(trend,lang="en",count=200, tweet_mode="extended")
    for t in tweets:
      tweet_info = dict()
      tweet_info["id"] = t.id_str
      tweet_info["img_url"] = t.user.profile_image_url_https
      tweet_info["created_at"] = t.created_at
      tweet_info["user"] = t.user.screen_name
      tweet_info["Tweet"] = t.full_text
      tweets_array.append(tweet_info)
  return tweets_array



#predict saltiness


def predict_saltiness(text):
  xtemp = pipeline.transform([text])
  predictions = model.predict(xtemp)
  return round(predictions[0]*100,2)

#get_top_10
def get_top_10(tweets_array):
  saltiness = []
  for i,t in enumerate(tweets_array):
    t['saltiness'] = predict_saltiness(t["Tweet"])
    saltiness.append(t)
  saltiness.sort(key = lambda x:(x['saltiness']),reverse=False)
  return saltiness[:10]

def prepare_top_10():
    trending = get_trending()
    tweets_array = get_tweets(trending)
    top_10 = tweets_array[:10]
    top_10 = get_top_10(tweets_array)
    return top_10


#if main test
if __name__ == "__main__":
    #trending = get_trending()
    #tweets_array = get_tweets(trending)
    #print(len(tweets_array))
    ########top_10 = get_top_10(tweets_array)
    top_10 = prepare_top_10()
    print(top_10)