#!/usr/bin/env python
import os
import sys
import time
import urllib
import random
import logging
from datetime import datetime, timedelta, date
try:
    import endpoints
except ImportError:
    from google.appengine.ext import endpoints
from google.appengine.ext import ndb
from google.appengine.api import mail
from google.appengine.api import users
from google.appengine.api import files
from google.appengine.api import search
from google.appengine.ext import deferred
from google.appengine.api import urlfetch
from google.appengine.ext.webapp import template
from google.appengine.api import channel as gchannel
from google.appengine.api.datastore_types import BlobKey
from google.appengine.api.images import get_serving_url
from google.appengine._internal.django.utils import simplejson as json
import jinja2

logger = logging.getLogger(__name__)

OWNER = 'kelonyemitchel@gmail.com'

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

APP = {
  'title': 'GCS Demo',
  'description': '',
  'keywords': '',
  'gcs': {
    'bucket': 'test-kelonye'
  }
}
