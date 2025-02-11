# express.js

## create a HTTP server using express.js

```shell
npm install express@4
```

```js
// index.js

// Import the 'express' module, which is used to create a web server
const express = require('express');

// Create an instance of the express application
const server = express();

// Define the port the server will listen on
const port = 3000;

// Define a route for HTTP GET requests to the '/hello' URL path
server.get('/hello', function (req, res) {
    // When this route is accessed, send the 'Hello World!' response
    res.send('Hello World!');
});

// Start the server and listen on the specified port (3000)
// Once the server starts, log a message to the console
server.listen(port, function () {
    console.log('Listening on ' + port);  // This logs when the server is ready to accept requests
});
```

and run it

```shell
node index.js
```
