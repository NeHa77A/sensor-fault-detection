# common code
from sensor.exception import SensorException
from sensor.logger import logging
import os, sys, yaml, dill
import numpy as np

def read_yaml_file(file_path:str) ->dict:
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise SensorException(e,sys)    
    
# write yaml file
def write_yaml_file(file_path:str, content: object, replace:bool=False)->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path,"w") as file:
            yaml.dump(content,file)
    except Exception as e:
        raise SensorException(e,sys) 
    
def save_numpy_array_data(file_path:str,array:np.array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            np.save(file_obj,array)
    except Exception as e:
        raise SensorException(e,sys)
    
def load_numpy_array_data(file_path:str)->np.array:
    try:
        with open(file_path,"rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise SensorException(e,sys)
    
def save_object(file_path:str, obj:object)->None:
    try:
        logging.info("Entered tha save_object function of main_util")
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
        logging.info("Exited tha save_object fun of main_utils")
    except Exception as e:
        raise SensorException(e,sys)
    
def load_object(file_path:str)->object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"file path :{file_path} is not exist")
        with open(file_path,"rb") as file_obj:
            dill.load(file_obj)
            return dill
    except Exception as e:
        raise SensorException(e,sys)