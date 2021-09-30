# Pandas Ex.5
import pandas as pd
import numpy as np
from pandas.core import series
from pandas.core.indexes.base import Index 
import quandl
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm

# load my API key.
api_key = open('quandlapikey.txt','r').read()

BODYVBMS = quandl.get("OECD/HEALTH_LVNG_BODYVBMS_TOTPOPTX_GBR", authtoken=api_key)
FOODCALT = quandl.get("OECD/HEALTH_LVNG_FOODCALT_CALPERQT_GBR", authtoken=api_key)

print(BODYVBMS.head())
print(FOODCALT.head())

BODYVBMS.columns = ["% Obese or Overweight"]        # change the column name
FOODCALT.columns = ["Kcal Per Capita Per Day"]      # change the column name

        #  Use df1.join(df2) to join these two dfs by their index.
joined = pd.merge(BODYVBMS, FOODCALT, on='Date')
print(joined.head())
'''
            % Obese or Overweight  Kcal Per Capita Per Day
Date
1980-12-31                   36.0                   3116.0
1987-12-31                   41.0                   3227.0
1991-12-31                   49.0                   3208.0
1992-12-31                   50.0                   3271.0
1993-12-31                   52.9                   3218.0'''

count_nan = joined.isna().sum()  
print("No of null values: ",count_nan)
print('Total missing values: '+str(joined.isnull().values.sum()))
   #   What is the standard deviation of the mean calorie intake in the UK?
std_joined = joined["Kcal Per Capita Per Day"].std(ddof=0)     
print("\n STD: %.2f"  %std_joined)     # 2 numbers after the dot 91.71

joined_corr = joined.corr()
print("\n correlation:\n", joined_corr)

'''
correlation:
                          % Obese or Overweight  Kcal Per Capita Per Day
% Obese or Overweight                 1.000000                 0.889723
Kcal Per Capita Per Day               0.889723                 1.000000

the R square value helps determine how well the model is blend and how well the output value is explained
 by the determining(independent) variables of the dataset. The value of R square ranges between [0,1]'''

squared_correlation = joined.corr()**2          # 0.791607
print("\n coefficient : \n", squared_correlation)

df = joined.dropna()            # Drop null values                     
x = df['% Obese or Overweight']
y = df['Kcal Per Capita Per Day']

res = stats.linregress(x, y)     # Perform the linear regression
print(f"R-squared: {res.rvalue**2:.6f}")    # 0.791607 same as line 37.....

#     add the regression line to your df (add a column called Y')
d = np.polyfit(x,y,1)     # 1=linear regression  [  12.50664216 2632.0562191 ]
f = np.poly1d(d)(x)          # provide us with a function that will do the fitting.
print(len(f))
f1 = pd.Series(f)
print('f1:', f1)        # has numbers but....next adds Nan
df['Y'] = f1           # add a column for the regression line called Y TODO - adds Nan


# SciPy method to generate line formula,  R2  etc
# Generated linear fit
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
line = slope*x+intercept
df["YY"] = line
print(df.head())

# statsmodels supports specifying models using R-style formulas and pandas DataFrames.TODO explain...
df['Eins'] = np.ones(( len(df), ))
print(df.head())
Y = df['% Obese or Overweight'][:-1]
X = df[['Kcal Per Capita Per Day','Eins']][:-1]
result = sm.OLS( Y, X ).fit()
print("R-squared = %.3f" % result.rsquared)
print("regress", result)

#Draw a scatter plot of Calorie intake vs. Obesity, add the best fit line and show its formula and R-squered 
fig, ax=plt.subplots()     # Add a figure and set your axis
plt.scatter(x,y, alpha=0.5)
plt.plot(x, f, "r")
plt.plot(x, line, "yellow")
plt.xlabel('% Obese or Overweight')
plt.ylabel('Kcal Per Capita Per Day')
        # set axes limits
ylim = [30,70]
xlim = [3100, 3450]
        # add text to the line plot
r_squared = np.round(r_value**2, decimals=2)
mu = np.round(df["Kcal Per Capita Per Day"].mean(), decimals=2)
#plt.text(min(X), 63, '$\mu={0}$ \n$R^2={1}$'.format(mu, r_squared), fontsize=17)   #TODO fix
#plt.text(min(X), 60, '$y={0}*x{1}$'.format(np.round(slope, decimals=2),np.round(intercept, decimals=2)), fontsize=17)

plt.legend().remove()
ax.set_ylabel('% Obese or Overweight', fontsize=16)
ax.set_xlabel("Kcal Per Capita Per Day", fontsize=16)

# place a text box in upper left in axes coords
ax.text(0.15, 0.08, r_squared, transform=ax.transAxes, fontsize=10,
        verticalalignment='top')
plt.show()

