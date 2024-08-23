import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.operations import SearchIndexModel

# Connect to your Atlas deployment

uri = "mongodb+srv://olegalkina:6uyfIuCq0dB1rKMI@@myatlasclusteredu.pnon21i.mongodb.net/?retryWrites=true&w=majority&appName=myAtlasClusterEDU""

client = MongoClient(uri)

# Access your database and collection

database = client["movies"]
collection = database["movies_records"]

from pymongo.operations import SearchIndexModel

search_index_model = SearchIndexModel(
  definition={
    {
 "fields": [
   {
     "numDimensions": 256,
     "path": "embedding",
     "similarity": "cosine",
     "type": "vector"
    }
   ]
  }
 },
  name="vector_index",
  type="vectorSearch",
)

result = collection.create_search_index(model=search_index_model)
print(result)
