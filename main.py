from sensor.configuration.mongoDB_connection import MongoDBClient
from sensor.exception import SensorException
import sys,os
from sensor.logger import logging
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainPipeline
from fastapi import FastAPI
from sensor.constant.application import APP_HOST, APP_POST
from starlette.responses import RedirectResponse
from uvicorn import run as app_run
from fastapi.responses import Response
from sensor.ml.model.estimator import ModelResolver
from sensor.constant.training_pipeline import SAVED_MODEL_DIR
from sensor.ml.model.estimator import ModelResolver, TragetValueMapping
from sensor.utils.main_utils import load_object
from fastapi.middleware.cors import CORSMiddleware

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

if __name__=='__main__':
    training_pipeline_config =TrainingPipelineConfig()
    data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
    print(data_ingestion_config.__dict__)
"""
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        train_pipeline = TrainPipeline()
        if train_pipeline.is_pipeline_running:
            return Response("Training pipeline is already running.")
        train_pipeline.run_pipeline()
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")

@app.get("/predict")
async def predict_route():
    try:
        df=None
        model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        if not model_resolver.is_model_exists():
            return Response("Model is not available")
        
        best_model_path = model_resolver.get_best_model_path()
        model = load_object(file_path=best_model_path)
        y_pred = model.predict(df)
        df['predicted_column'] = y_pred
        df['predicted_column'].replace(TragetValueMapping().reverse_mapping(),inplace=True)
              
    except Exception as e:
        raise Response(f"Error Occured! {e}")
def main():
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)
if __name__=='__main__':
    #app_run(app, host=APP_HOST, port=APP_POST)
    main()