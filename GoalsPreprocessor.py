import pandas as pd

from DataPreprocessor import DataPreprocessor
from config import goals_col_mappings

class GoalsPreprocessor(DataPreprocessor):
    
    def __init__(self, batch_id, data):
        super().__init__(batch_id)
        self.data = self.preprocess(data)

    def preprocess(self, data):
        data = self.standardize_col_names(data)
        data = self.remap_col(data)
        data = self.prepend(data, 'region', 'portfolio_id')

        return data

    def remap_col(self, data):
        """
        Create Strategy ID Column
        """
        data['strategy_id']= data['goal_type'].apply(lambda x: goals_col_mappings[x])
        return data

    def prepend(self, data, col_1, col_2):
        """
        Prepend col_1 with col_2 to overwrite col_2
        """
        data[col_2] = data[col_1] + data[col_2]
        return data
