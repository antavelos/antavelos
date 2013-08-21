import webapp2
from . import JINJA_ENVIRONMENT

class Main(webapp2.RequestHandler):

    def get(self):        
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())