import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from pandas.core.indexes.base import Index
import scipy.stats as stats
import seaborn as sns
from seaborn.categorical import boxplot


# Read the file
df = pd.read_excel('D:\Documents\יעל\Python\Final_Project\SIS_Burns.xlsx', index_col=0)   # without an index

df = df.drop('name', axis=1)     # drop the 'name' column
print(df.head(3))
group_pig = df.groupby('pig')     # group by pigs
print(group_pig.first())          # prints the first entry of every pig
g_pig_side = df.groupby(['pig', 'side', 'Burn_time'])    # # group by pig no., side of body and burn time
print(g_pig_side.first())

# Pivot table - calculate the mean per pig per side for each burn time
table = pd.pivot_table(df, values=['Day_0', 'Day_1', 'Day_2','Day_3','Day_4','Day_5','Day_7'], index=['pig', 'side'],
                    columns=['Burn_time'], aggfunc=np.mean). round(2)       # round(2) for 2 decimal places
print(table.head())               
table_transpose =  table.transpose()              # transpose the table
print('table transpose:\n', table_transpose)                 


#                Boxplot graph
#--------------------------------------------
# seaborn plots:
table_dict = table.to_dict()      # store vectors in a Python dictionary to assigning names of their columns
#print(table_dict)
table = table.reset_index()      # reset index to prevent multi-indexing!!!
print(table.head())    
ax = sns.boxplot(data=table)
ax = sns.swarmplot(data=table, color=".10", size=3)     # Use swarmplot() to show the datapoints on top of the boxes
plt.show()

sns.boxplot(data=table.transpose())
sns.swarmplot(data=table.transpose(), color=".10", size=3)
plt.show()

#Slicing DF per pig:
#pig372 = 


'''
#        iterating through groups:
for day, bTime in table:
    print(day, bTime)
'''    
#        One-Way Anova
# -----------------------------------------
# # stats f_oneway functions takes the groups as input and returns F and P-value
# fvalue, pvalue = stats.f_oneway(d['A'], d['B'], d['C'], d['D'])
# print(fvalue, pvalue)



#                Boxplot graph
#--------------------------------------------
#fig, axes = plt.subplots(3, 2, sharey=True)    # 3 rows, 2 columns
# table.boxplot(column=['Day_0'])     # working on 3 first rows
# plt.show()





# cross-tabulation: Test if 'side' is expected to affect the 


#g_pig_side.boxplot(subplots=False)
# aggregation and creating mean
# ax = g_pig_side.boxplot(g_pig_side)
# plt.show()
# work only with rows of pig 372:


#p372 = df[df['372']]
#df_grouped['Group'].agg(['mean', 'std'])

# print(df_grouped.head())
# print(df_grouped.describe())
# ax = df_grouped.boxplot(df_grouped)       # The subplots=False option shows the boxplots in a single figure.
# plt.title("Rat IgM fold 14 days after vaccination")
# plt.ylabel('IgM Fold from day 0')
# plt.show()
