# Pandas ex2

import pandas as pd

df = pd.read_csv('D:\Python\pandas\microsoft_workers.csv', index_col='User Name') # set 'user name as index
df.rename(columns={'Display Name': 'Nickname'}, inplace=True)                # replace Display Name with 'Nickname
print(df.head(3))
df.to_csv('new_csv.csv')
df.to_csv('new_html.html')

df = pd.read_csv('D:\Python\pandas\microsoft_workers.csv')
