'''
Given a pandas dataframe with class label column named 'class', 
it will sample from each class
'''

import pandas as pd

# read in data
df = pd.read_csv('airline_sample.csv')

# create class label
df['class'] = df['flight_search'].str.extract('((?<=Class=).{1})')
classes = list(df['class'].unique())
num_samples = [5, 1, 3, 1]

def stratified_sample(labels, num):
    # now sample from each and put in list
    sampled_dfs = []
    
    for c, num in zip(labels, num):
        # sample only specified class in specified amount, and put it in the list
        sampled_dfs.append(df[df['class'] == c].sample(num))
    
    # concat the list into one dataframe
    return pd.concat(sampled_dfs, axis=0, ignore_index=True)

print(stratified_sample(classes, [2, 1, 3, 1]))
