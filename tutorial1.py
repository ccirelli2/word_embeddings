# -*- coding: utf-8 -*-
"""
Ref:
    https://towardsdatascience.com/introduction-to-word-embedding-and-word2vec-652d0c2060fa
    https://towardsdatascience.com/a-beginners-guide-to-word-embedding-with-gensim-word2vec-model-5970fa56cc92
    https://github.com/zhlli1/Genism-word2vec/blob/master/Genism%20Word2Vec%20Tutorial.ipynb
"""

# Python Modules --------------------------------------------------------------
import pandas as pd

# Directories -----------------------------------------------------------------
dir_data = r'C:\Users\chris.cirelli\Desktop\repositories\word_embeddings\data'

# Load Data -------------------------------------------------------------------
df = pd.read_csv(dir_data + '/' + 'data.csv')
print(df.head())


# Data Preparation ------------------------------------------------------------
''' Gensim requires a list of lists where each list comprises a document within
    which is a list of words or tokens from that document. 
        
'''

# Create New Column Make + Model
df['Make+Model'] = df['Make'] + ' ' + df['Model']

print(df.head())


