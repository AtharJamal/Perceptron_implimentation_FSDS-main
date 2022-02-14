import pandas as pd

import logger


class data_getter():
    def __init__(self,file_object,logger_object):
        self.training_file='Training_files_from_DB/dataset_small.csv'
        self.logger_object=logger.App_Logger()
        self.file_object=open("data_reading_log.txt",'a+')
    def data_read(self):
        self.logger_object.log(self.file_object,"About to start the file reading operation")
        try:
            data = pd.read_csv(self.training_file)
            self.logger_object.log(self.file_object,"Data Load Successful.Exited the get_data method of the Data_Getter class")
            return data
        except:
            self.logger_object.log(self.file_object, "Exception occured at data_read method of data_getter class")
            self.logger_object.log(self.file_object, "Data Load Unsuccessful.Exited the data_read method of the Data_Getter class")
            raise Exception()