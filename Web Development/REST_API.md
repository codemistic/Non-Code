<h1 align="center">
Application Package Interface:
</h1>

An API is a set of programming code that enables data transmission between one software product and another. It also contains the terms of this data exchange.
Examples can be 
- Fetching details about the flight timing between any two from database
- for making payments and updating the database



## REST API :
REST stands for REpresentational State Transfer API.It is an architectural style of designing an API with a set of constraints and rules.
REST API is a way of accessing web services in a simple and flexible way without having any processing.

Rules regarding REST architecture:

- Use appropiate HTTP Verbs
Basically there are four HTTPS methods
  - GET :- Reading the data from the server(or database)
  - POST :- Refers to creating a new record in database.
  - PUT/PATCH :- Refers to updating the entry in the databse.
  - DELETE :- Refers to deleting the entry in database.

- Using appropiate route functions : Use appropiate route functiond for the puro=pose of routing requests.

### Sample REST API:

We will be designing API for the purpose of managing articles of technology using our local database on localhost machine .

  - Database used : MongoDB (WikiDB in our case)
  - Tools : NPM, VisualCode and Node.js
  - For testing the server used : POSTMAN (a good option)



### Here's how app.js file looks :

```
//jshint esversion:6

const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const mongoose = require("mongoose");

const app = express();

app.set("view engine", "ejs");

app.use(
  bodyParser.urlencoded({
    extended: true,
  })
);
app.use(express.static("public"));
//mongoose connection to local_host
mongoose.connect("mongodb://localhost:27017/WikiDB", {
  useNewUrlParser: true,
});
//Defining Schema
const wikiapi = mongoose.Schema({
  title: {
    type: String,
    required: true,
  },
  Description: {
    type: String,
    required: true,
  },
});
// Creating Collection
const Article = mongoose.model("Article", wikiapi);

/------------------------ Working on all articles ------------------------/

app.get("/articles", function (req, res) {
  Article.find(function (err, data) {
    if (err) {
      res.send(err);
    } else {
      res.send(data);
    }
  });
});

app.post("/articles", function (req, res) {
  var name = req.body.title;
  var des = req.body.Description;
  var article1 = new Article({
    title: name,

    Description: des,
  });
  article1.save();
  console.log("Inserted");
});

app.delete("/articles", function (req, res) {
  Article.deleteMany(function (err) {
    if (err) res.send(err);
    else res.send("DELETED");
  });
});

/------------------------ Working on Specific Article ------------------------/

app // using chained calling of routes
  .route("/articles/:Title")
  .get(function (req, res) {
    Article.findOne({ title: req.params.Title }, function (err, doc) {
      if (err) {
        res.send(err);
      } else {
        res.send(doc);
      }
    });
  })
  .put(function (req, res) {
    Article.updateMany(
      { title: req.params.Title },
      { title: req.body.title, Description: req.body.Description },
      function (err) {
        if (err) {
          res.send(err);

          console.log(err);
        } else {
          res.send("Updated the article");
        }
      }
    );
  })
  .patch(function (req, res) {
    Article.updateMany(
      { title: req.params.Title },
      { $set: { title: req.body.title, Description: req.body.Description } },
      function (err) {
        if (err) res.send(err);
        else res.send("Updated the article");
      }
    );
  })
  .delete(function (req, res) {
    Article.deleteMany({ title: req.params.Title }, function (err) {
      if (err) res.send(err);
      else res.send("Deleted the article");
    });
  });
// Starting the server
app.listen(3000, function () {
  console.log("Server started on port 3000");
});

```
