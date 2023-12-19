from pymongo import MongoClient

### Local database ###
# db_client = MongoClient().local


### Connect local db to Mongo Atlas.
url = "mongodb+srv://alpaca:alpacamexicanA@cluster0.cro8pnx.mongodb.net/?retryWrites=true&w=majority"
db_client = MongoClient(url).alpaca
