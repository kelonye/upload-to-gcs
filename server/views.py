import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "lib")))

try:
    import endpoints
except ImportError:
    from google.appengine.ext import endpoints
from google.appengine.ext import blobstore
from google.appengine.api import users
from webapp2_extras import sessions
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine._internal.django.utils import simplejson as json

import webapp2 as webapp
from protorpc import remote

import models

sessions.default_config['secret_key'] = 'dev'


class View(webapp.RequestHandler):

    pass


class IndexView(View):

    def get(self):
        template_values = {
            'app': models.APP
        }
        template = models.JINJA_ENVIRONMENT.get_template(
            'templates/index.html'
        )
        self.response.write(template.render(template_values))

app = webapp.WSGIApplication([
    ('/', IndexView),
], debug=True)
