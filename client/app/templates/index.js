[
  'application',
  'application/error',
  'application/index',
].forEach(function(t){
  var v = './'+t.replace('/', '-');
  var k = t.replace('application/', '');
  Em.TEMPLATES[k] = Em.Handlebars.compile(require(v));
});
