## What is a NoSQL database?
When people use the term “NoSQL database,” they typically use it to refer to any non-relational database. Some say the term “NoSQL” stands for “non SQL” while others
say it stands for “not only SQL.” Either way, most agree that NoSQL databases are databases that store data in a format other than relational tables.
## Brief history of NoSQL databases
NoSQL databases emerged in the late 2000s as the cost of storage dramatically
decreased. Gone were the days of needing to create a complex, difficult-to-manage
data model in order to avoid data duplication. Developers (rather than storage) were
becoming the primary cost of software development, so NoSQL databases optimized for
developer productivity.
s storage costs rapidly decreased, the amount of data that applications needed to store
and query increased. This data came in all shapes and sizes — structured,
semi-structured, and polymorphic — and defining the schema in advance became
nearly impossible. NoSQL databases allow developers to store huge amounts of
unstructured data, giving them a lot of flexibility.
Additionally, the Agile Manifesto was rising in popularity, and software engineers were
rethinking the way they developed software. They were recognizing the need to rapidly
adapt to changing requirements. They needed the ability to iterate quickly and make
changes throughout their software stack — all the way down to the database. NoSQL
databases gave them this flexibility.
Cloud computing also rose in popularity, and developers began using public clouds to
host their applications and data. They wanted the ability to distribute data across
multiple servers and regions to make their applications resilient, to scale out instead of
scale up, and to intelligently geo-place their data. Some NoSQL databases like
MongoDB provide these capabilities.

## NoSQL database features
Each NoSQL database has its own unique features. At a high level, many NoSQL
databases have the following features:
● Flexible schemas
● Horizontal scaling
● Fast queries due to the data model
● Ease of use for developers
## Types of NoSQL databases
Over time, four major types of NoSQL databases emerged: document databases,
key-value databases, wide-column stores, and graph databases.
● Document databases store data in documents similar to JSON (JavaScript
Object Notation) objects. Each document contains pairs of fields and values. The
values can typically be a variety of types including things like strings, numbers,
booleans, arrays, or objects.
● Key-value databases are a simpler type of database where each item contains
keys and values.
● Wide-column stores store data in tables, rows, and dynamic columns.
● Graph databases store data in nodes and edges. Nodes typically store
information about people, places, and things, while edges store information about
the relationships between the nodes

## Understanding Differences in the Four Types of NoSQL Databases

NoSQL databases use a different approach. Based on a data model there are a few types of
databases in the NoSQL world. Here are the five main types of NoSQL databases:

1. Key-value stores
2. Column-oriented databases
3. Document databases
4. Graph databases
5. Multi-Model Databases

MongoDB, CouchDB, CouchBase, Cassandra, HBase, Redis, Riak, Neo4J are the popular NoSQL
databases examples.
MongoDB, CouchDB, CouchBase , Amazon SimpleDB, Riak, Lotus Notes are Document-oriented
NoSQL databases.
Tokyo Cabinet/Tyrant, Redis, Riak, Voldemort, Oracle BDB, Amazon SimpleDB are Key-value
stores Databases.
Cassandra, HBase and Hypertable are Column family stores Databases.
Neo4J, InfoGrid, Infinite Graph, OrientDB, FlockDB are Graph databases. Lets discuss these types
of databases in detail.

1. Key-Values Stores
The main idea here is using a hash table where there is a unique key and a pointer to a particular
item of data. The Key/Value model is the simplest and easiest to implement. But it is inefficient when
you are only interested in querying or updating part of a value, among other disadvantages.
Key-value pair storage databases store data as a hash table where each key is unique, and the
value can be a JSON, BLOB(Binary Large Objects), string, etc.
Key-value stores store everything as a key and a value.
The value in a key-value store can be anything: a string, a number, but also an entirely new set of
key-value pairs encapsulated in an object. Figure 6 shows a slightly more complex key-value
structure.
Examples: Tokyo Cabinet/Tyrant, Redis, Voldemort, Oracle BDB, Amazon SimpleDB, Riak
Key-value nested structure.

2. Column Family Stores
These were created to store and process very large amounts of data distributed over many
machines. There are still keys but they point to multiple columns. The columns are arranged by
column family.
They deliver high performance on aggregation queries like SUM, COUNT, AVG, MIN, etc. as the
data is readily available in a column.
Column-based NoSQL databases are widely used to manage data warehouses, business
intelligence, CRM, Library card catalogs.
Examples: Cassandra, HBase, Hypertable

3. Document Databases
These were inspired by Lotus Notes and are similar to key-value stores. The model is basically
versioned documents that are collections of other key-value collections. The semi-structured
documents are stored in formats like JSON. Document databases are essentially the next level of
Key/value, allowing nested values associated with each key. Document databases support querying
more efficiently. Newspapers or magazines, for example, contain articles. To store these in a relational database, you
need to chop them up first: the article text goes in one table, the author and all the information about
the author in another, and comments on the article when published on a website go in yet another.
As shown below, a newspaper article can also be stored as a single entity; this lowers the cognitive
burden of working with the data for those used to seeing articles all the time.
Examples: CouchDB, MongoDb, Amazon SimpleDB, Riak, Lotus Notes

4. Graph Databases
Instead of tables of rows and columns and the rigid structure of SQL, a flexible graph model is used
which, again, can scale across multiple machines. NoSQL databases do not provide a high-level
declarative query language like SQL to avoid overtime in processing. Rather, querying these
databases is data-model specific. Many of the NoSQL platforms allow for RESTful interfaces to the
data, while other offer query APIs.
Compared to a relational database where tables are loosely connected, a Graph database is a
multi-relational in nature. Traversing relationships as fast as they are already captured into the DB,
and there is no need to calculate them.
Graph base databases mostly used for social networks, logistics, spatial data.
Node—: The entities themselves. In a social network this could be people.
Edge: The relationship between two entities. This relationship is represented by a line and has its
own properties. An edge can have a direction, for example, if the arrow indicates who is whose boss.
Graphs can become incredibly complex given enough relation and entity types. Graph databases
like Neo4j also claim to uphold ACID, whereas document stores and key-value stores adhere to
BASE.
Examples: Neo4J, InfoGrid, Infinite Graph, OrientDB, FlockDB

5. Multi-Model Databases
Multi-model databases are designed to handle multiple data models against a single integrated
backend. They are a brand-new in the NoSQL world, and there will be much more buzz around this
type of database in the future.

OrientDB, for example, is a multi-model database, combining NoSQL types. OrientDB is graph
database where each node is a document.
The possibilities are endless, and because the world is becoming increasingly interconnected, graph
databases are likely to win terrain over the other types, including the still-dominant relational
database. A ranking of the most popular databases and how they’re progressing can be found at
http://db-engines.com/en/ranking.

Figure – Top 15 databases ranked by popularity according to DB-Engines.com in Jan 2022.

## Some of the Free and Open Source NoSQL Databases

NoSQL databases are becoming popular day by day. I have come up with the list of best, free and
open source NoSQL databases. MongoDB tops the list of Open Source NoSQL databases. This list
of free and open source databases comprises MongoDB, Cassandra, CouchDB, Hypertable,
Redis, Riak, Neo4j, HBASE, Couchbase, MemcacheDB, RevenDB and Voldemort. These free
nosql database list and open source NoSQL databases are really highly scale-able, flexible and
good for big data storage and processing. These open source NoSQL databases are far ahead in
terms of performance as compared to traditional relational databases.
The global NoSQL Database Market was valued USD 3.5 Billion in 2019 and is anticipated to reach
USD 21 Billion by 2026, expanding at a CAGR of 31.4% during the forecast period 2020-2026. The
growth of the market is attributed to the increasing implementation of Big Data among various
industry verticals. Moreover, the growing awareness of NOSQL benefits for various web applications
is stimulating market growth.
NoSQL also called “Not Only SQL” facilitates the storage and retrieval of data in a non-relational
database format. Unlike, a relational database (RDBMS), NoSQL allows the related to be structure
in a unified structure. The widespread adoption of these databases proliferated after the 2000s
owing to the decreased cost of the storage and the increasing data processing requirements.

Furthermore, NoSQL has a dynamic schema that makes them feasible for content management
systems, real-time analytics, and a rise in unstructured data applications.

However, these may not be always the best choice for you. Most of common applications can still be
developed using traditional relational databases. NoSQL databases are still not the best option for a
mission critical transaction needs. We have listed down a small description of all these best free
NoSQL datbase and open source NoSQL databases. Lets have a look.

1. MongoDB
MongoDB is a document-oriented database that uses a JSON-style data format. It’s ideal for website
data storage, content management and caching applications, and can be configured for replication
and high availability.
This highly scale-able and agile NoSQL database is a amazing performing system. This NoSQL
open source database written in C++ comes with a storage that is document oriented. Also, you will
be provided with benefits like full index support, high availability across WANs and LANs along with
easy replication, horizontal scaling, rich queries that are document based, flexibility in data
processing and aggregation along with proper training, support and consultation.

2. Cassandra
An Apache Software Foundation project, Cassandra is a distributed database that allows for
decentralized data storage that is fault tolerant and has no single point of failure. In other words,
“Cassandra is suitable for applications that can’t afford to lose data.”

3. CouchDB
A product of the Apache Software Foundation, CouchDB is another document-oriented database
that stores data in free JSON database format. It’s ACID compliant, and like MongoDB, can be used
to store data and content for websites, and to provide caching. You can use JavaScript to run
MapReduce Queries on CouchDB. It also provides a very convenient web based administration
console. This database could be really handy for web applications.

4. Hypertable
Modeled after Google’s BigTable database system, Hypertable’s creators aim for it to be the “open
source standard for highly available, petabyte scale, database systems.” In other words, Hypertable
is designed for storing massive amounts of data reliably across many cheap servers.

5. Redis
This is an open source nosql, key value store of an advanced level. Owing to the presence of
hashes, sets, strings, sorted sets and lists in a key; Redis is also called as a data structure server.
This system will help you in running atomic operations like incrementing value present in a hash, set
intersection computation, string appending, difference and union. Redis makes use of in-memory
dataset to achieve high performance. Also, this system is compatible with most of the programming
languages.

6. Riak
Riak is one of the most powerful, distributed databases ever to be introduced. It provides for easy
and predictable scaling and equips users with the ability for quick testing, prototyping and application
deployment so as to simplify development.

7. Neo4j
This is a NoSQL graph database which exhibits a high level of performance. It comes well equipped
with all the features of a robust and mature system. It provides the programmers with a flexible and
object oriented network structure and allows them to enjoy all the benefits of a database that is fully
transactional. Compared to RDBMS, Neo4j will also provide you with performance improvements on
some of the applications.

8. Hadoop HBASE
HBase can be easily considered as a scalable, distributed and a big data store. This database can
be used when you are looking for real time and random access to your data. It comes with modular
and linear scalability along with reads and writes that are strictly consistent. Other features include
Java API that has an easy client access, table sharing that is configurable and automatic, Bloom
filters and block caches and much more.

9. Couchbase
While Couchbase was a fork of CouchDB, it has become more of a full-fledged data product and
less of a ball of framework than CouchDB. Its transition to a document database will give MongoDB
a run for its money. It is multithreaded per node, which can be a major scalability benefit —
especially when hosted on custom or bare-metal hardware. With some nice integration features,
including with Hadoop, Couchbase is a great choice for an operational data store.

10. MemcacheDB
MemcacheDB is a distributed storage system of key value. It should not be confused with a cache
solution; rather, it is a persistent storage engine which is meant for data storage and retrieval in a
fast and reliable manner. Confirmation to memcache protocol is provided for. The storing backend
that is used is the Berkeley DB which supports features like replication and transaction.

11. REVENDB
RAVENDB is a second generation open source DB. This DB is document oriented and schema free
such as you simply have to dump in your objects into it. It provides extremely flexible and fast
queries. This application makes scaling extremely easy by providing out-of-the-box support for
replication, multi tenancy and sharding. There is full support for ACID transactions along with safety
of your data. Easy extensibility via bundles is provided along with high performance.
