from abc import abstractmethod
import pandas as pd
import string
import re

class DataPreprocessor:
    
    def __init__(self, batch_id):
        self.batch_id = batch_id

    @abstractmethod
    def preprocess(self, data):
        return

    def standardize_col_names(self, data, remove_punct=True):
        """ 
        Converts all column names to lower case replacing
        whitespace of any length with a single underscore.
        Also, remove punctuations if included.
        
        """

        translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))

        for c in data.columns:
            
            c_mod = c.lower()
            
            if remove_punct:            
                c_mod = c_mod.translate(translator)
            
            c_mod = '_'.join(c_mod.split(' '))
            
            if c_mod[-1] == '_':
                c_mod = c_mod[:-1]
            
            c_mod = re.sub(r'\_+', '_', c_mod)
            
            data.rename({c: c_mod}, inplace=True, axis=1)

        return data
