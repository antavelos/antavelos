import webapp2
from instagram.client import InstagramAPI
from . import JINJA_ENVIRONMENT

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