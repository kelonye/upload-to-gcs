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
import cloudstorage as gcs

sessions.default_config['secret_key'] = 'dev'


GCS_BUCKET = os.environ.get('BUCKET_NAME', app_identity.get_default_gcs_bucket_name())


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


class ClientView(View):

    def get(self):
        template_values = {
            'app': models.APP
        }
        template = models.JINJA_ENVIRONMENT.get_template(
            'templates/client.html'
        )
        self.response.write(template.render(template_values))


class ServerView(View):

    def get(self):

        image = None
        upload_url = None

        if self.request.get('image'):
            image = '/server/serve/' + self.request.get('image')

        else:
            upload_url = blobstore.create_upload_url('/server/upload', gs_bucket_name=GCS_BUCKET)
            
        template_values = {
            'app': models.APP,
            'image': image,
            'upload_url': upload_url,
        }
        template = models.JINJA_ENVIRONMENT.get_template(
            'templates/server.html'
        )
        self.response.write(template.render(template_values))


class ServerUploadView(blobstore_handlers.BlobstoreUploadHandler):

    def post(self):

        upload = self.get_uploads()[0]

        self.redirect('/server/serve/%s' % upload.key())


class ServerServeView(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, key):
        if not blobstore.get(key):
            self.error(404)
        else:
            self.send_blob(key)


app = webapp.WSGIApplication([
    ('/', IndexView),
    ('/client', ClientView),
    ('/server', ServerView),
    ('/server/upload', ServerUploadView),
    ('/server/serve/([^/]+)?', ServerServeView),
], debug=True)
