import pandas as pd
df = pd.read_csv('textdatei.json') # can replace with df = pd.read_table('input.txt') for '\t'
df.to_excel('output.xlsx', 'Sheet1')