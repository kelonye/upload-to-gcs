[
  'gcs-upload',
].forEach(function(t){
  var mod = './' + t.replace('/', '-');
  Em.TEMPLATES['components/'+t] = Em.Handlebars.compile(require(mod));
});
