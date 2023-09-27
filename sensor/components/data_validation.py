from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
from sensor.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from sensor.entity.config_entity import DataValidationConfig
from sensor.logger import logging
from sensor.exception import SensorException
import pandas as pd
import sys,os
from sensor.utils.main_utils import read_yaml_file

class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact, data_validation_config:DataValidationArtifact):
        try:
            self.data_ingestion_artifact =data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise SensorException(e,sys)
        

# Number of columns
    def validate_number_of_columns(self, dataframe:pd.DataFrame)->bool:
        try:
            Number_of_columns=self._schema_config["columns"]
            if len(dataframe.columns)== Number_of_columns:
                return True
            return False
        except Exception as e:
            raise SensorException(e,sys)
        
    def drop_zero_std_columns(self,dataframe):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)

    def is_numerical_column_exist(self,dataframe:pd.DataFrame)->bool:
        try:
            numerical_columns=self._schema_config["numerical_columns"] 
            dataframe_columns = dataframe.columns
            numerical_column_present = True
            missing_numerical_columns =[]
            for num_column in numerical_columns:
                if num_column not in dataframe_columns:
                    numerical_column_present = False
                    missing_numerical_columns.append(num_column)
            logging.info(f"missing numerical column : [{missing_numerical_columns}]")
            return numerical_column_present
        except Exception as e:
            raise SensorException(e,sys)

    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise SensorException(e,sys)

    def detect_data_drift(self):
        pass
    
    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            err_message =""
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
            # read data from test and train file location
            train_dataframe =DataValidation.read_data(train_file_path)
            test_dataframe =DataValidation.read_data(test_file_path)

            # validation of number of columns
            status =self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                err_message= f"{err_message}Train dataframe does not contain all column \n"
            status =self.validate_number_of_columns(dataframe=test_dataframe)
            if not status:
                err_message= f"{err_message}Test dataframe does not contain all column \n"

            # validate mumerical column
            status = self.is_numerical_column_exist(dataframe=train_dataframe)
            if not status:
                err_message= f"{err_message}Train dataframe does not contain all numerical column\n"
            status = self.is_numerical_column_exist(dataframe=test_dataframe)
            if not status:
                err_message= f"{err_message}Test dataframe does not contain all numerical column \n"

            if len(err_message)>0:
                raise Exception(err_message)
            
            # data Drift

        except Exception as e:
            raise SensorException(e,sys)