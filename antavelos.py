from google.appengine.api import users
import webapp2
import os
import jinja2
import sys
from pprint import pprint
import json

sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

from pattern.web import Twitter
from pattern.web.locale import geocode 
from instagram.client import InstagramAPI


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
    extensions=['jinja2.ext.autoescape'])

class MainPage(webapp2.RequestHandler):

    def get(self):        
        template_values = {
            'greetings': 'Hello',
            'guestbook_name': 'Alex',
            'url': 'www.example.com',
            'url_linktext': 'my link',
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

class Tweets(webapp2.RequestHandler):

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


class Instapairs(webapp2.RequestHandler):

    def get(self):
        images = []
        api = InstagramAPI(client_id='e33a8515b0cc4bc8aef4e7b086b736b1', client_secret='b50e5753efaa40ff8953e24fb8126616')
        popular_media = api.media_popular(count=15)
        for media in popular_media:
            images.append(media.images['standard_resolution'].url)

        template_values = {
            'images': images,
        }

        template = JINJA_ENVIRONMENT.get_template('instapairs.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/tweets', Tweets),
    ('/geotweet', GeoTweet),
    ('/instapairs', Instapairs)
], debug=True)