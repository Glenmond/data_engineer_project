import pandas as pd
import pickle
import datetime
from config import outputs_mappings

batch_id = datetime.date.today().strftime("%y%m%d")

class DataExporter:

    def __init__(self, batch_id, data_dict):
        self.directory = outputs_mappings
        self.data_dict = data_dict # dict of df
        self.batch_id = batch_id

    def export_to_csv(self):
        """
        Load dataframe back to csv files
        """
        for k, v in self.directory.items():
             self.data_dict[k].to_csv(f"outputs/{batch_id}_{v}", index=False)
        
    def export_to_pickle(self):
        """
        Load dataframe back to pickle files
        """
        for k, v in self.directory.items():
             self.data_dict[k].to_pickle(f"outputs/{batch_id}_{v}")
