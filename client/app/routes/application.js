/**
  * Module dependencies.
  */
var store = App.store;


App.ApplicationRoute = Em.Route.extend({

  setupController: function(c, m){
    this._super(c, m);
    c.setup(m);
  },
  
  actions: {

    notify: function(type, msg, hideIn){
      var self = this;
      this.controllerFor('application').set(type, msg);
      if (hideIn){
        setTimeout(function(){
          self.send('unnotify', type);
        }, hideIn * 1000);
      }
    },

    unnotify: function(type){
      this.controllerFor('application').set(type, null);
    },

    reloadApp: function(){
      window.location.assign('/#');
    },

    voteHunt: function(hunt){
      this.controllerFor('application').send('voteHunt', hunt);
    },

    previewHunt: function(hunt){
      this.controllerFor('application').send('previewHunt', hunt);
    },

  },

});