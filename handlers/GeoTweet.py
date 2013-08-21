import webapp2
import json
from pattern.web import Twitter
from pattern.web.locale import geocode 
from . import JINJA_ENVIRONMENT

class GetTweets(webapp2.RequestHandler):

    def get(self):
        lat = float(self.request.get('lat'))
        lng = float(self.request.get('lng'))
        term = self.request.get('term')
        # api = Api(consumer_key='XdtvreY2svkoTY5XYw3D7A', 
        #     consumer_secret='LwscpqCRO8FN8vnxQAykJ61YiU03AlLQWoZM2PKmgk', 
        #     access_token_key='226700305-fXVoTnL1sp3HWWrST8YIXRrFHK0OipF1cQwPupGH', 
        #     access_token_secret='Y11hi28YFL3e5cl3OmzpNQeD1wWt2Hb1bHZd7GTyQw')
        
        twitter = Twitter(language='en')
        tweets = []
        for tweet in twitter.search('obama', geo=(lat, lng)):
            tweets.append(tweet.text)
        
        data = {"tweets": tweets} 
        self.response.write(json.dumps(data))
        
        # template = JINJA_ENVIRONMENT.get_template('index.html')
        #self.response.write(template.render(template_values))

class GeoTweet(webapp2.RequestHandler):

    def get(self):        
        template = JINJA_ENVIRONMENT.get_template('geotweet.html')
        self.response.write(template.render())
