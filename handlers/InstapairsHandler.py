import webapp2
from . import JINJA_ENVIRONMENT
import models.Instapairs as Insta


class Instapairs(webapp2.RequestHandler):

    def get(self):

        pairs = Insta.Instapairs()
        images = pairs.getPopularImages('thumbnail', 15)

        template_values = {
            'images': images,
        }

        template = JINJA_ENVIRONMENT.get_template('instapairs.html')
        self.response.write(template.render(template_values))