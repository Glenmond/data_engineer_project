import pandas as pd
import tzlocal

from datetime import datetime
from DataPreprocessor import DataPreprocessor

class PerformancePreprocessor(DataPreprocessor):
    
    def __init__(self, batch_id, data):
        super().__init__(batch_id)
        self.data = self.preprocess(data)

    def preprocess(self, data):
        data = self.standardize_col_names(data)
        data = self.col_rename(data)
        data['calc_date'] = data['calc_date'].apply(lambda x: self.convert_to_local_time(x))
        data = self.nav_filter(data)
        
        return data

    def convert_to_local_time(self, value):
        """
        Convert unix timestampe to required date format
        Return a string formatted date
        """
        unix_timestamp = float(value)
        local_timezone = tzlocal.get_localzone() # get pytz timezone
        local_time = datetime.fromtimestamp(unix_timestamp, local_timezone)
        
        local_time = local_time.strftime("%m,%d,%Y,%H:%M")
        
        return local_time
    
    def col_rename(self, data):
        """
        Rename columns to standardise with other classes
        """
        data.rename(columns={"portfolioid": "portfolio_id", "calcdate": "calc_date", "officialnav": "official_nav"}, inplace=True)
        return data

    def nav_filter(self, data):
        """
        Value > 1000 as True and Value <= 1000 as False
        """
        data['above_1000'] = data['official_nav'].apply(lambda x: True if x > 1000 else False )
        return data