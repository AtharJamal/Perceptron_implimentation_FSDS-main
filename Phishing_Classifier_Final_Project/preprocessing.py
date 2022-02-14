import numpy as np
class preprocessor():
    def __init__(self,file_object,logger_object):
        self.file_object=file_object
        self.log_writer=logger_object

    def remove_column_all_zero(self,data):
        self.data=data
        self.log_write.log(self.file_object,"Starting the process of removal of columns having all values as zero")
        try:
            for i in self.data.columns:
                if (self.data[i] == 0).all():
                    self.data.drop(i,axis=1,inplace=True)
                    self.log_write.log(self.file_object,"Removed columns with all values as zero")
                else:
                    pass
            return self.data
        except Exception as e:
            self.log_write.log(self.file_object,"Exception occured in remove_column_all_zero method of the Preprocessor class. Exception message:  "+str(e))
            self.log_write.log(self.file_object,"Column removal Unsuccessful. Exited the remove_column_all_zero method of the Preprocessor class")
            raise Exception()
    def remove_column_missing_value(self,data):
        self.data = data
        self.log_write.log(self.file_object, "Starting the process of removal of all columns having 90% missing values")
        try:
            for i in self.data.columns:
                if (np.divide((self.data[i] == (-1)).sum(), len(self.data)) > 0.90):
                    self.data.drop(i,axis=1,inplace=True)
                    self.log_write.log(self.file_object, "Removed columns having 90% missing values")
                else:
                    pass
            return self.data
        except Exception as e:
            self.log_write.log(self.file_object,"Exception occured in remove_column_missing_value method of the Preprocessor class. Exception message:  "+str(e))
            self.log_write.log(self.file_object,"Column removal Unsuccessful. Exited the remove_column_missing_value method of the Preprocessor class")
            raise Exception()

    def remove_columns_higher_correlation(self,data):
        self.data=data
        col_corr = set()
        cor_matrix = self.data.corr()
        try:
            for i in range(len(cor_matrix.columns)):
                for j in range(i):
                    if abs(cor_matrix.iloc[i, j]) > 0.90:
                        colname = cor_matrix.columns[i]
                        col_corr.add(colname)
                    else:
                        pass
            self.data.drop(col_corr, axis=1, inplace=True)
            return self.data
        except Exception as e:
            self.log_write.log(self.file_object,"Exception occured in remove_columns_higher_correlation method of the Preprocessor class. Exception message:  "+str(e))
            self.log_write.log(self.file_object,"Column removal Unsuccessful. Exited the remove_columns_higher_correlation method of the Preprocessor class")
            raise Exception()