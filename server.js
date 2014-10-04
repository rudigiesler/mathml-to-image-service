// server.js

// Setup
var express = require('express');
var bodyparser = require('body-parser');
var app = express();

app.use(bodyparser.urlencoded({ extended: true }));
app.use(bodyparser.json());

var port = process.env.PORT || 8080;        // set the port

// Routes
var router = express.Router();
router.get('/', function(req, res) {
    res.json({ message: 'Hello, world!' });   
});

// Register routes
app.use('/', router);

app.listen(port);
console.log('Listening on ' + port);
