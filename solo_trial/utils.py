from pymongo import MongoClient
"""
#alt 1
import mongoengine
mongoengine.connect(db=db_name, host=hostname, username=username, password=pwd)

#alt 2
from pymongo import MongoClient
def get_db_handle(db_name, host, port, username, password):

    client = MongoClient(host=host,
                    port=int(port),
                    username=username,
                    password=password
                    )
    db_handle = client['db_name']
    return db_handle, client

#alt 3
from pymongo import MongoClient
client = pymongo.MongoClient('connection_string')
db = client['db_name']

connection_string = mongodb+srv://<username>:<password>@<atlas cluster>
/<myFirstDatabase>?retryWrites=true&w=majority
"""

connection_string = 'mongodb://localhost:27017/'
client = MongoClient(connection_string)
db = client['django']

