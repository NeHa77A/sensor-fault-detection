from sensor.configuration.mongoDB_connection import MongoDBClient

if __name__ =='__main__':
    mongodb_client=MongoDBClient()
    print("collection name: ",mongodb_client.database.list_collection_names())