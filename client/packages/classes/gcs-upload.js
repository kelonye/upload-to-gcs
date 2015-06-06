/**
 * Module dependencies
 */
var upload = require('ember-upload');
var slug = require('slug');


var GCS = {
};

GCS.url = 'https://'+CONFIG.gcs.bucket+'.storage.googleapis.com/';

App.GcsUploadComponent = Em.Component.extend({

  init: function(){

    var self = this;
    var key = slug((new Date).toISOString());
    var opts = {
      'Content-Type': 'image/png',
      'key': key,
      'success_action_status': '201',
    };

    this.upload = upload(GCS.url, opts);
    this.upload.addObserver('upload.loadend', function(){
      Em.run.later(function(){
        var path = GCS.url + key;
        console.log('GCS path: %s', path);
        self.set('path', path);
      }, 2000);
    });

    this._super();

  },

});