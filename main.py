from sensor.configuration.mongoDB_connection import MongoDBClient
from sensor.exception import SensorException
import sys,os
from sensor.logger import logging
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig

"""
def test_exce():
    try:
        logging.info("We are diving by zero")
        x =1/0
    except Exception as e:
        raise SensorException(e,sys)
if __name__ =='__main__':
    try:
        test_exce()
    except Exception as e:
        print(e)
    #mongodb_client=MongoDBClient()
    #print("collection name: ",mongodb_client.database.list_collection_names())
"""
if __name__=='__main__':
    training_pipeline_config =TrainingPipelineConfig()
    data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
    print(data_ingestion_config.__dict__)