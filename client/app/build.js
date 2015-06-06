/**
  * Module dependencies.
  */
var fs = require('fs');
var path = require('path');
var builder = require('component-hooks');
var cwd = path.join(__dirname);
var out = path.join(__dirname, '/../../public');
var dev = '1' !== process.env.MINIFY;

// exec

var build = builder(cwd)
  .out(out)
  .name('app')
  .copy()
  .standalone();

if (dev) build.dev();

build.end(function(err){
  if (err) throw err;
});