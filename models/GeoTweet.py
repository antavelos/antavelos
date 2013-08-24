from pattern.web import Twitter
from pattern.web.locale import geocode 

class GeoTweet:

    def getTweetsByCoord(self, term, lat, lng):
        
        twitter = Twitter(language='en')
        tweets = []
        for tweet in twitter.search('traffic', geo=(lat, lng)):
            tweets.append(tweet.text)

        return tweets