from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.artifact_entity import DataValidationArtifact , ModelTrainerArtifact, ModelEvaluationArtifact, ModelPusherArtifact
from sensor.entity.config_entity import ModelEvaluationConfig, ModelPusherConfig
import os, sys
from sensor.ml.model.estimator import SensorModel
import shutil


class ModelPusher:
    def __init__(self,model_pusher_config:ModelPusherConfig,model_evaluation_artifact:ModelEvaluationArtifact):
        try:
            self.model_pusher_config= model_pusher_config
            self.model_evaluation_artifact = model_evaluation_artifact
        except Exception as e:
            raise SensorException(e,sys)
        
    def initiate_model_pusher(self,)->ModelPusherArtifact:
        try:
            trained_model_path = self.model_evaluation_artifact.trained_model_path
            model_file_path =self.model_pusher_config.model_file_path
            os.makedirs(os.path.dirname(model_file_path), exist_ok=True)
            shutil.copy(src=trained_model_path,dst=model_file_path)
            
            #save model path
            save_model_path = self.model_pusher_config.save_model_path
            os.makedirs(os.path.dirname(save_model_path), exist_ok=True)
            shutil.copy(src=trained_model_path,dst=save_model_path)

            # prepare artifact
            model_pusher_artifact=ModelPusherArtifact(
                saved_model_path=save_model_path,
                model_file_path=model_file_path
            )
            return model_pusher_artifact


        except Exception as e:
            raise SensorException(e,sys)
