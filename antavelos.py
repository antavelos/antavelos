import webapp2
import handlers.MainHandler as Main
import handlers.GeoTweetHandler as Geotweet
import handlers.InstapairsHandler as Instapairs
import handlers.RpsHandler as Rps


app = webapp2.WSGIApplication([
    ('/', Main.Main),
    ('/tweets', Geotweet.GetTweets),
    ('/geotweet', Geotweet.GeoTweet),
    ('/instapairs', Instapairs.Instapairs),
    ('/rock-paper-scissors', Rps.Rps)
], debug=True)