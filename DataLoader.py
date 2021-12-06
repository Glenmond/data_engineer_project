import pandas as pd
import datetime
from config import inputs_mappings

batch_id = datetime.date.today().strftime("%y%m%d")

class DataLoader:

    def __init__(self, start_dt):
        self.directory = inputs_mappings
        self.data_dict = self.load_data()

    def load_data(self):
        """
        Returns dictionary of dataframes
        """
        data_dict = {}
        for k, v in self.directory.items():
            data_dict[k] = pd.read_csv(v)
        
        return data_dict