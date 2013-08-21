import webapp2
import handlers.Main as Main
import handlers.GeoTweet as Geotweet
import handlers.Instapairs as Instapairs


app = webapp2.WSGIApplication([
    ('/', Main.Main),
    ('/tweets', Geotweet.GetTweets),
    ('/geotweet', Geotweet.GeoTweet),
    ('/instapairs', Instapairs.Instapairs)
], debug=True)