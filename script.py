##Imports
import pandas as pd 
import numpy as np 
import sqlalchemy as sa 
from sqlalchemy import create_engine
from pandas.util import hash_pandas_object
import os
import time
import datetime
import yaml

##Open Yaml Config file in reading mode
with open('config.yaml', 'r') as config_file:
    config = yaml.load(config_file, Loader=yaml.FullLoader)
##SQL Connection Params
server  = config['server']
db = config['db']
table1 = config['table1']
table2 = config['table2']

engine = sa.create_engine(f'mssql+pyodbc://{server}/{db}?Trusted_Connection=yes&Driver=ODBC Driver 17 for SQL Server')
con = engine.connect()

##Get shape of the DF
shape = df.shape
rows = shape[0]
cols = shape[1]

##Create 2 dataframes from the sql tables
df1 = pd.read_sql_table(table1, con=con)
df2 = pd.read_sql_table(table2, con=con)

##Hash the 2 dataframes
h1 = hash_pandas_object(df1)
h2 = hash_pandas_object(df2)

##Get number of matching rows
num_matching_rows = h[h == h1].count()

##Print num of matching out of total rows
print(f"There are {num_matching_rows} matching rows out of {rows} rows")