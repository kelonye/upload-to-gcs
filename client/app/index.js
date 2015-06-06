/**
  * Module dependencies.
  */
require('ember');

// app

window.App = Em.Application.create({

});

App.moment = require('moment');
App.store = require('store');
App.batch = require('batch');

require('./templates');
require('./models');
require('./views');
require('./controllers');
require('./routes');

// local

require('global');
require('partials');
require('packages');

// router

App.Router.map(function(){
});
