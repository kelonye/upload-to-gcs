/**
  * Module dependencies.
  */
var store = App.store;


App.IndexRoute = Em.Route.extend({

  setupController: function(c, m){
    this._super(c, m);
    c.setup(m);
  },

});