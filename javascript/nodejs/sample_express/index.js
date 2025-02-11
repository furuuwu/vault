const express = require('express');
const server = express();
const port = 3000;

server.get('/', function (req, res) {
    res.send('This is the root endpoint...');
});
server.get('/hello', function (req, res) {
    res.send('Hello World!');
});
server.listen(port, function () {
    console.log('Listening on ' + port);
});