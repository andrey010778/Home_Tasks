import numpy as np
import pandas as pd

article_read = pd.read_csv('c:/data/orderdata_sample.csv', sep = ',')

article_read['Total'] = article_read['Quantity'] * article_read ['Price'] + article_read['Freight']

df_new = article_read[['OrderID', 'Total']]

print(df_new)

article_read.to_csv('c:/data/orderdata_sample_1.csv')

