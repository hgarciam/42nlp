import nltk
from nltk import sent_tokenize
from random import randint
import tweepy
import time

nltk.download('punkt')
nltk.download('stopwords')


def run_marvin():

    consumer_key = "8fJkRQraedTvio7p1iQDoMe4k"
    consumer_secret = "BYRRx7gLuC7JLvalzb5YP50fCDBW2qbLeYVjYtzUlGqQkHFL14"

    key = "1391679453428916224-J4CRPrcMiYwvmhHxqJqwsSPIju28Sm"
    secret = "mTVRTJBjWYL6RaKOlTx3ryc7J2OleSiI3qLy8CJZGrTv1"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Reply to mention

    FILE_NAME = 'last_seen_tweet.txt'
    elon_tweets = 'elon_last_seen.txt'

    text_file = open('text.txt')
    text = text_file.read()
    sentences = sent_tokenize(text)

    def read_last_seen(FILE_NAME):
        file_read = open(FILE_NAME, "r")
        last_seen_id = int(file_read.read().strip())
        file_read.close()
        return last_seen_id

    def store_last_seen(FILE_NAME, last_seen_id):
        file_write = open(FILE_NAME, "w")
        file_write.write(str(last_seen_id))
        file_write.close()
        return

    def generate_sentence():
        return sentences[randint(0, len(sentences))]

    #api.update_status("Welcome to the Hitchhiker's Guide to the Galaxy random sentence generator bot!")

    def reply():
        tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode="extended")
        length4tweet = False
        for tweet in tweets:
            while length4tweet == False:
                sentence = generate_sentence()
                if len(sentence) <= 280:
                    length4tweet = True

            #print(tweet.user.screen_name + ' - ' + str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + " " + sentence, tweet.id)
            #api.create_favorite(tweet.id)
            #api.retweet(tweet.id)
            print("@" + tweet.user.screen_name + ", " + sentence)
            store_last_seen(FILE_NAME, tweet.id)

    def periodic_sentence():
        length4tweet = False
        while length4tweet == False:
            sentence = generate_sentence()
            if len(sentence) <= 280:
                length4tweet = True
        api.update_status(sentence)
        print(sentence)

    def reply_to_elon():
        screen_name = "elonmusk"
        tweets = api.user_timeline(since_id=read_last_seen(elon_tweets), screen_name = screen_name, count=1, exclude_replies=True)
        length4tweet = False
        for tweet in tweets:
            while length4tweet == False:
                sentence = generate_sentence()
                if len(sentence) <= 280:
                    length4tweet = True
            print("Replying to Elon")
            print(tweet.user.screen_name + ' - ' + str(tweet.id) + ' - ' + tweet.text)
            #api.update_status("@" + tweet.user.screen_name + " " + sentence, tweet.id)
            #api.create_favorite(tweet.id)
            print(sentence)
            store_last_seen(elon_tweets, tweet.id)

    timecount = 0
    while True:
        reply()
        reply_to_elon()
        time.sleep(15)
        timecount += 15
        if timecount > 30:
            periodic_sentence()
            timecount = 0


if __name__ == '__main__':
    run_marvin()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
