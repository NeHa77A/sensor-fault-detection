import os
from sensor.constant.S3_bucket import TRAINING_BUCKET_NAME

## Define common constant
TARGET_COLUMN = "class"
# we name of pipeline
PIPELINE_NAME:str ="sensor"
ARTIFACT_DIR:str ="artifact"
FILE_NAME:str ="sensor.csv"
TRAIN_FILE_NAME:str ="train.csv"
TEST_FILE_NAME: str = "test.csv"

PREPROCESSING_OBJECT_FILE_NAME ="preprocessing.pkl"
MODEL_FILE_NAME ="model.pkl"
SCHEMA_FILE_PATH =os.path.join("config","schema.yaml")
SCHEMA_DROP_COLS = "drop_columns"

# constant for Data ingestion
DATA_INGESTION_COLLECTION_NAME:str ="sensor"
DATA_INGESTION_DIR_NAME:str ="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str ="feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float = 0.2    # 20% test data

# Constant for Data Vlaidation
DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_VALID_DIR:str = "valideted"
DATA_VALIDATION_INVALID_DIR:str ="invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str ="drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str ="report.yaml"

# constant for data transformation
DATA_TRANSFORMTION_DIR_NAME:str ="data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR:str ="transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR:str = "transformed_object"