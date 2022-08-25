#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

class DataFrameInfo():
    def __init__(self, df):
        self.df = df.copy()

    def get_columns_list(self):
       
        return self.df.columns.to_list()

    def detail_info(self):
       
        print(self.df.info())

    def null_column_percentage(self):
        num_rows, num_columns = self.df.shape
        df_size = num_rows * num_columns
        
        null_size = (self.df.isnull().sum()).sum()
        percentage = round((null_size / df_size) * 100, 2)
        print(f"The Telecom data contains { percentage }% missing values.")

    def get_null_counts(self):
        print(self.df.isnull().sum())

    def skewness(self):
        print(self.df.skew())


# In[ ]:




