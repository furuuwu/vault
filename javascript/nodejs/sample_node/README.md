# HTTP server

## create a HTTP server (with the built-in http library)

```js
// index.js

const http = require('http');  // Import the built-in 'http' module

// Define the server
const server = http.createServer((req, res) => {
    // Set the response HTTP header
    res.statusCode = 200;  // Status code 200 indicates success
    res.setHeader('Content-Type', 'text/plain');  // Set response type as plain text

    // Send the response body "Hello, World!"
    res.end('Hello, World!\n');
});

// Set the server to listen on port 3000
const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
});
```

and run it

```shell
node index.js
```

test it - once the server is running, open your browser or use a tool like curl

```shell
curl http://localhost:3000
```

## resources

* <https://www.w3schools.com/nodejs/>
