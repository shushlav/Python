import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}      # a dictionary

df = pd.DataFrame(web_stats)
print(df)
print(df.head)    # print the first 5
print(df.tail(2)) # print the last 2

df = pd.read_csv('D:\Python\pandas\EOD-HD.csv')
df.set_index('Date', inplace=True)  #מבטל מיספור והופך את התאריך לאינדקס
print(df.head())

df['Volume'].to_csv('newcsv2.csv')  #  שמירה של עמודה אחת בלבד לקובץ בנוסף לאינדקס
df = pd.read_csv('newcsv2.csv', index_col=0)  # put the first column as index
print(df.head())
df.columns = ['Stock volumes']   # change the columns name
print(df.head())
df.to_html('newhtml.html')       # Save as html file
df.to_csv('newcsv_no_headers.csv', header=False)   # Save without headers
df = pd.read_csv('newcsv_no_headers.csv', names=['Date','stock_volume'])    # open and add headers
print(df.head(2))
df.rename(columns={'stock_volume':'Shares_volume'}, inplace=True)  # change only one column head
print(df.head(1))

