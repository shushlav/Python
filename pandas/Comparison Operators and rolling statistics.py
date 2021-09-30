#    Comparison Operators


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

bridge_height = {'meters':[10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}   # one point is an outlier
#  create a df
df = pd.DataFrame(bridge_height)
# plot the df
df.plot()      # we  can see the outlier
plt.show()

# How can we detect it automaticly?
# using std

df['STD'] = df['meters'].rolling(2).std()    # std of every 2 points
print(df)
#  כשנדע מהי סטיית התקן ההמוצעת נוכל להחליט איזה נתון גבוה ממנה ושיש לסלקו
df_std = df.describe()
print(df_std)
'''           meters          STD
count     9.000000     8.000000
mean    699.394444  1096.419446
std    2067.384584  2030.121949
min      10.220000     0.007071
25%      10.250000     0.026516
50%      10.270000     0.035355
75%      10.310000  1096.425633
max    6212.420000  4385.610607
'''
df_std = df.describe()['meters']['std']
print("mean sts:", df_std)    # mean sts: 2067.3845835687607

df = df[df['STD'] < df_std * 2]    # we'll get only the info that is not outlier AUTOMATOCLY!
print(df)
'''
  meters       STD
1   10.31  0.035355
2   10.27  0.028284
3   10.22  0.035355
4   10.23  0.007071
7   10.25  0.021213
8   10.31  0.042426
'''



df.plot()
plt.show()