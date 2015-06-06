[
].forEach(function(t){
  var mod = './' + t.replace('/', '-');
  Em.TEMPLATES['partials/'+t] = Em.Handlebars.compile(require(mod));
});
