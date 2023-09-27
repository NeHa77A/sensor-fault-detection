from sklearn.impute import SimpleImputer
import sys
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from imblearn.combine import SMOTETomek
from sklearn.preprocessing import RobustScaler
from sensor.constant.training_pipeline import TARGET_COLUMN
from sensor.entity.artifact_entity import DataTransformationArtifact, DataValidationArtifact
from sensor.entity.config_entity import DataTransformationConfig
from sensor.ml.model.estimator import TragetValueMapping
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils.main_utils import save_numpy_array_data, save_object


class DataTransformation:
    def __init__(self, data_validation_artifact:DataValidationArtifact, data_transformation_config:DataTransformationConfig):
        try:
            self.data_validation_artifact = data_validation_artifact
            self.data_transformation_config = data_transformation_config
        except Exception as e:
            raise SensorException(e,sys)
        
    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise SensorException(e,sys)
        
    @classmethod
    def get_data_transformer_object(cls)->Pipeline:
        try:
            robust_scaler = RobustScaler()
            simple_imputer = SimpleImputer(strategy="constant", fill_value=0)

            preprocessor =Pipeline(
                steps=[("Imputer",simple_imputer),
                ("RobustScaler",robust_scaler)]
            )
        except Exception as e:
            raise SensorException(e,sys)
        
    def initiate_data_transformation(self)->DataTransformationArtifact:
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)