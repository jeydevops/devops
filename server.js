var http = require('http');
//loads http module
var app=http.createServer(function (req, res) {
//creates server
  res.writeHead(200, {'Content-Type': 'text/plain'});
  //sets the right header and status code
  res.end('Hello Viewer!!! Welcome to our Amazon NodeJS DevOps Demo...\n');
  //outputs string with line end symbol
}).listen(80, "ec2-54-237-64-198.compute-1.amazonaws.com");
//sets port and IP address of the server
console.log('Server running at http://ec2-54-237-64-198.compute-1.amazonaws.com:80/');
