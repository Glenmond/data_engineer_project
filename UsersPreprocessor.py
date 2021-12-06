import pandas as pd

from DataPreprocessor import DataPreprocessor

class UsersPreprocessor(DataPreprocessor):
    
    def __init__(self, batch_id, data):
        super().__init__(batch_id)
        self.data = self.preprocess(data)

    def preprocess(self, data):
        data = self.standardize_col_names(data)
        data = self.split_name(data)
        data = self.drop_cols(data, ['email'])
        
        return data

    def split_name(self, data):
        """
        Split the name field into first_name and last_name
        """
        data[['first_name','last_name']] = data['full_name'].loc[data['full_name'].str.split().str.len() == 2].str.split(expand=True)
        return data

    def drop_cols(self, data, col_list):
        """
        Drop unnecessary columns
        """
        data.drop(col_list, axis=1, inplace=True)
        return data