/**
  * Module dependencies.
  */

Em.TextSupport.reopen({
  attributeBindings: ['required', 'maxlength']
});


[
].forEach(function(mod){
  require('./'+mod);
});
