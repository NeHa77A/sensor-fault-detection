import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi
ca = certifi.where()

class MongoDBClient:
    client =None

    def __init__(self, database_name=DATABASE_NAME) ->None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url ="mongodb+srv://Neha:Neha@cluster0.jsogkox.mongodb.net/"
                """
                mango_db_url =os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment Key: {MONGODB_URL_KEY} is not set.")
                """
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            #raise SensorException(e,sys)
            raise e
        