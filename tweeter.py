import tweepy
import config


client = tweepy.Client(consumer_key=config.API_Key,
                       consumer_secret=config.API_Key_Secret,
                       access_token=config.Access_Token,
                       access_token_secret=config.Access_Secret)

post = "I can't wait to send more tweets with the API!"

# send tweet with client.create_tweet method and text as argument. Save the result in a variable called response
response = client.create_tweet(text=tweet)
print(response)