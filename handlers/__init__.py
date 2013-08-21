import sys
import os
import jinja2

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/models')
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/lib')

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/templates'),
    extensions=['jinja2.ext.autoescape'])