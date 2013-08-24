import webapp2
import json
import models.GeoTweet as GTweet
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
        
        GT = GTweet.GeoTweet()
        tweets = GT.getTweetsByCoord(term, lat, lng)
        
        data = {"tweets": tweets} 
        self.response.write(json.dumps(data))
        

class GeoTweet(webapp2.RequestHandler):

    def get(self):        
        template = JINJA_ENVIRONMENT.get_template('geotweet.html')
        self.response.write(template.render())
