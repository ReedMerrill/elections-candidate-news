import pandas as pd

df = pd.read_csv('ab2021_elec.csv')

names = df['first_name'] + ' ' + df['last_name']

df.to_csv('names.csv')
