import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split

from src.components.data_transformation import Datatransformation
from src.components.data_transformation import DataTransformationConfig


'''
The dataclasses module in Python provides a decorator and functions for automatically adding special methods 
such as __init__() and __repr__() to user-defined classes. 
This module was introduced in Python 3.7 to simplify the creation of classes that primarily store data.
'''

from dataclasses import dataclass

class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv') # path to save train data
    test_data_path:str = os.path.join('artifacts','test.csv') # path to save test data
    raw_data_path:str = os.path.join('artifacts','data.csv') # path to save initial data
    
    
class Dataingestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # all 3 paths will be saved in ingestion_config
    
    # intitate data from outer source eg: mongodb,sql server    
    def initiate_data_ingestion(self): 
        logging.info("Enter the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv') # reading the data
            logging.info('Read the dataset as dataframe')
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("train-test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Ingestion of data completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj = Dataingestion()
    train_data,test_data = obj.initiate_data_ingestion()
    
    data_transformation = Datatransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)
    
############### use this command to run the file -> python -m src.components.data_ingestion         
