import webapp2
from . import JINJA_ENVIRONMENT

class Rps(webapp2.RequestHandler):

    def get(self):        
        template = JINJA_ENVIRONMENT.get_template('rps.html')
        self.response.write(template.render())