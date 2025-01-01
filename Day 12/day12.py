import tweepy
import random

API_KEY = "9BbRu0PVyskeoH5nJWC9w55mS"
API_SECRET = "XAx3C25jXZXPPlw58YW9xpqYlcqIqQ1eJK7xB89MiWQ7XeGkb4"
ACCESS_TOKEN = "1852292686004301825-TWS5dCzC0sB20v1LsdzDo0Pvu4eJSU"
ACCESS_TOKEN_SECRET = "KjAZKm1sh7NDhVJp82Dqha6XN9yaoApBVhP9m5rQe3TdG"


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

tweet_links = [
    "https://x.com/THEAIRDROPARC/status/1873799074279023047",
    "https://x.com/THEAIRDROPARC/status/1873799131891982431",
    # "https://x.com/THEAIRDROPARC/status/1873799284052898195",
    # "https://x.com/THEAIRDROPARC/status/1873799331716927773",
]

comments = [
    "$CAT is going to the moon.",
    "wen listing $CAT in HL?",
    "$HAPPY is the one that I'll be getting this new year."
    "$HAPPY is here to stay"
]


for link in tweet_links:
    try:
        tweet_id = link.split("/")[-1]
        comment = random.choice(comments)
        api.update_status(status=comment, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)
        print(f"Commented on {link} with: '{comment}'")
    except tweepy.TweepyException as e:
        print(f"Error commenting on {link}: {e}")
