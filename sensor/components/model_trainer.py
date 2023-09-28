from sensor.utils.main_utils import load_numpy_array_data
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.artifact_entity import DataTransformationArtifact , ModelTrainerArtifact
from sensor.entity.config_entity import ModelTrainerConfig
import os, sys
from xgboost import XGBClassifier
from sensor.ml.metric.classification_metric import get_classification_score
from sensor.ml.model.estimator import SensorModel
from sensor.utils.main_utils import save_object,load_object

class ModelTrainer:
    def __init__(self, model_trainer_config:ModelTrainerConfig, data_tansformation_artifact:DataTransformationArtifact):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_tansformation_artifact = data_tansformation_artifact
        except Exception as e:
            raise SensorException(e,sys)
    
    def initiate_model_training(self)->ModelTrainerArtifact:
        try:
            #load traineing array and test array
            train_file_path=self.data_tansformation_artifact.transformed_train_file_path
            test_file_path=self.data_tansformation_artifact.transformed_test_file_path
            train_arr =load_numpy_array_data(train_file_path)
            test_arr = load_numpy_array_data(test_file_path)

            X_train, y_train, X_test, y_test =(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )
            model =self.train_model(X_train,y_train)

            y_train_pred = model.predict(X_train)
            classification_train_metric=get_classification_score(y_true=y_train,y_pred=y_train_pred)
            if classification_train_metric.f1_score<= self.model_trainer_config.expected_accuracy:
                raise Exception("Train model is not providing excepted accuracy.")
            
            y_test_pred = model.predict(X_test)
            classification_test_metric=get_classification_score(y_true=y_test,y_pred=y_test_pred)

            # check overfitting and underfitting
            difference =abs(classification_train_metric.f1_score - classification_test_metric.f1_score)
            if difference>self.model_trainer_config.overfitting_underfitting_thresold:
                raise Exception("Model is not efficient do more evalution")
            
            preprocessor = load_object(file_path=self.data_tansformation_artifact.transformed_object_file_path)
            model_dir_path = os.path.dirname(self.model_trainer_config.trained_model_file_path)
            os.makedirs(name=model_dir_path,exist_ok=True)
            sensor_model=SensorModel(preprocessor=preprocessor,model=model)
            save_object(self.model_trainer_config.trained_model_file_path, obj=sensor_model)
            
            # model trainer Artifact
            model_trainer_artifact =ModelTrainerArtifact(
                trained_model_file_path=self.model_trainer_config.trained_model_file_path,train_metric_artifact=classification_train_metric, test_metric_artifact=classification_test_metric)
            
            logging.info(f"Model Trainer artifact: {model_trainer_artifact}")
            return model_trainer_artifact

        except Exception as e:
            raise SensorException(e,sys)
        
    def train_model(self,X_train,y_train):
        try:
            xgb_clf = XGBClassifier()
            xgb_clf.fit(X_train,y_train)
            return xgb_clf
        except Exception as e:
            raise SensorException(e,sys)
        
    