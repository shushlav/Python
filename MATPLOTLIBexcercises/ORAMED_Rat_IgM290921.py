import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel('D:\Documents\יעל\Python\Final_Project\ORAMED_IgM.xlsx')

df['fold_14_days'] = df['Day 14'] / df['Day 0']

day14 = df[['Group', 'fold_14_days']]         # use onle group and fold for graphs
 
df_grouped = day14.groupby(by='Group')
#df_grouped['Group'].agg(['mean', 'std'])

print(df_grouped.head())
print(df_grouped.describe())
ax = df_grouped.boxplot(df_grouped)
plt.title("Rat IgM fold 14 days after vaccination")
plt.ylabel('IgM Fold from day 0')
plt.show()
