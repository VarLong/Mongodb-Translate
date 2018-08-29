> C:\Program Files\MongoDB\Server\4.0\data\ MongoDB zhu

 #Mongodb-Translate
Translate MongoDB api for Node.js. Original source：https://www.npmjs.com/package/mongodb 

Description:
The official MongoDB driver for Node.js. Provides a high-level API on top of mongodb-core that is meant for end users.
官方MongoDB驱动程序, Node.js, 为最终用户提供一个mongodb core的高级api.

NOTE: v3.x was recently released with breaking API changes. You can find a list of changes.
[最近发布的v3.x的API变化可以在下面的链接找到](https://github.com/mongodb/node-mongodb-native/blob/HEAD/CHANGES_3.0.0.md)

 ###MongoDB Node.JS Driver
>documentation: http://mongodb.github.io/node-mongodb-native
>api-doc: http://mongodb.github.io/node-mongodb-native/3.1/api
>source: https://github.com/mongodb/node-mongodb-native
>mongodb: http://www.mongodb.org

发现Bug, 报到这里：
https://jira.mongodb.org/secure/Dashboard.jspa

Change Log：
https://github.com/mongodb/node-mongodb-native/blob/HEAD/HISTORY.md

Installation：
The recommended way to get started using the Node.js 3.0 driver is by using the npm (Node Package Manager) to install the dependency in your project.
建议使用Node.js npm来安装mongoDB的依赖。

npm install mongodb --save
This will download the MongoDB driver and add a dependency entry in your package.json file.下载安装并添加依赖到package.json

 ##Connect to MongoDB
Create a new app.js file and add the following code to try out some basic CRUD operations using the MongoDB driver.
>Add code to connect to the server and the database myproject:

```javascript
const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');

// Connection URL
const url = 'mongodb://localhost:27017';

// Database Name
const dbName = 'myproject';

// Use connect method to connect to the server
MongoClient.connect(url, function(err, client) {
  assert.equal(null, err);
  console.log("Connected successfully to server");

  const db = client.db(dbName);

  client.close();
});

```
>Run your app from the command line with:
```javascript
node app.js
```
>Insert a Document
```javascript
const insertDocuments = function(db, callback) {
  // Get the documents collection
  const collection = db.collection('documents');
  // Insert some documents
  collection.insertMany([
    {a : 1}, {a : 2}, {a : 3}
  ], function(err, result) {
    assert.equal(err, null);
    assert.equal(3, result.result.n);
    assert.equal(3, result.ops.length);
    console.log("Inserted 3 documents into the collection");
    callback(result);
  });
}
```

The insert command returns an object with the following fields:
+result Contains the result document from MongoDB
+ops Contains the documents inserted with added _id fields
+connection Contains the connection used to perform the insert
>Add the following code to call the insertDocuments function:
```javascript
const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');

// Connection URL
const url = 'mongodb://localhost:27017';

// Database Name
const dbName = 'myproject';

// Use connect method to connect to the server
MongoClient.connect(url, function(err, client) {
  assert.equal(null, err);
  console.log("Connected successfully to server");
  const db = client.db(dbName);
  insertDocuments(db, function() {
    client.close();
  });
});
```
>Find All Documents
```javascript
const findDocuments = function(db, callback) {
  // Get the documents collection
  const collection = db.collection('documents');
  // Find some documents
  collection.find({}).toArray(function(err, docs) {
    assert.equal(err, null);
    console.log("Found the following records");
    console.log(docs)
    callback(docs);
  });
}
```
>This query returns all the documents in the documents collection. Add the findDocument method to the MongoClient.connect callback:
```javascript
const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');
 
// Connection URL
const url = 'mongodb://localhost:27017';
 
// Database Name
const dbName = 'myproject';
 
// Use connect method to connect to the server
MongoClient.connect(url, function(err, client) {
  assert.equal(null, err);
  console.log("Connected correctly to server");
 
  const db = client.db(dbName);
 
  insertDocuments(db, function() {
    findDocuments(db, function() {
      client.close();
    });
  });
});
```
>Find Documents with a Query Filter
```javascript
const findDocuments = function(db, callback) {
  // Get the documents collection
  const collection = db.collection('documents');
  // Find some documents
  collection.find({'a': 3}).toArray(function(err, docs) {
    assert.equal(err, null);
    console.log("Found the following records");
    console.log(docs);
    callback(docs);
  });
}
```
>Update a document
```javascript
const updateDocument = function(db, callback) {
  // Get the documents collection
  const collection = db.collection('documents');
  // Update document where a is 2, set b equal to 1
  collection.updateOne({ a : 2 }
    , { $set: { b : 1 } }, function(err, result) {
    assert.equal(err, null);
    assert.equal(1, result.result.n);
    console.log("Updated the document with the field a equal to 2");
    callback(result);
  });  
}
```
>The method updates the first document where the field a is equal to 2 by adding a new field b to the document set to 1. Next, update the callback function from MongoClient.connect to include the update method.
```javascript
const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');
 
// Connection URL
const url = 'mongodb://localhost:27017';
 
// Database Name
const dbName = 'myproject';
 
// Use connect method to connect to the server
MongoClient.connect(url, function(err, client) {
  assert.equal(null, err);
  console.log("Connected successfully to server");
 
  const db = client.db(dbName);
 
  insertDocuments(db, function() {
    updateDocument(db, function() {
      client.close();
    });
  });
});
```

>Remove a document
```javascript
const removeDocument = function(db, callback) {
  // Get the documents collection
  const collection = db.collection('documents');
  // Delete document where a is 3
  collection.deleteOne({ a : 3 }, function(err, result) {
    assert.equal(err, null);
    assert.equal(1, result.result.n);
    console.log("Removed the document with the field a equal to 3");
    callback(result);
  });    
}
```
Add the new method to the MongoClient.connect callback function.
```javascript
const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');
 
// Connection URL
const url = 'mongodb://localhost:27017';
 
// Database Name
const dbName = 'myproject';
 
// Use connect method to connect to the server
MongoClient.connect(url, function(err, client) {
  assert.equal(null, err);
  console.log("Connected successfully to server");
 
  const db = client.db(dbName);
 
  insertDocuments(db, function() {
    updateDocument(db, function() {
      removeDocument(db, function() {
        client.close();
      });
    });
  });
});
```
