var http = require('http');
//loads http module
var app=http.createServer(function (req, res) {
//creates server
  res.writeHead(200, {'Content-Type': 'text/plain'});
  //sets the right header and status code
  res.end('Hello World\n');
  //outputs string with line end symbol
}).listen(1337, "54.237.64.198");
//sets port and IP address of the server
console.log('Server running at http://54.237.64.198:1337/');
