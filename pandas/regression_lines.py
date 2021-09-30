import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from scipy import stats

np.random.seed(5)
# Create Xs and Ys
x = np.arange(1, 101)
y = 20 + 3 * x + np.random.normal(0, 60, 100)

np.random.seed(5)

# Create Xs and Ys
x = np.arange(1, 101)
y = 20 + 3 * x + np.random.normal(0, 60, 100)

# When you have your Xs and Ys, just print:
plt.plot(x, y)

d = np.polyfit(x,y,1)     # 1=linear regression   [ 3.01603092 24.6832371 ]  
f = np.poly1d(d)(x)       ## provide us with a function that will do the fitting.
# correlation
res = stats.linregress(x, y)
print(res)
'''
LinregressResult(slope=3.0160309214426197, intercept=24.683237099214296, 
rvalue=0.8416665841743692, pvalue=5.658546565371853e-28, stderr=0.19546745633809492, 
intercept_stderr=11.369923740717391)'''

r2 = res.rvalue**2
print("R**2:", r2)         # R**2: 0.7084026389157506

plt.plot(x, f)
plt.show()

'''       statsmodels
statsmodels is a Python module that provides classes and functions for the estimation 
of many different statistical models, as well as for conducting statistical tests, 
and statistical data exploration. '''

# Fit regression model
results = sm.OLS(y, x).fit()
# Inspect the results
print(results.summary())

'''                                 OLS Regression Results
=======================================================================================
Dep. Variable:                      y   R-squared (uncentered):                   0.922
Model:                            OLS   Adj. R-squared (uncentered):              0.921
Method:                 Least Squares   F-statistic:                              1173.
Date:                Wed, 09 Jun 2021   Prob (F-statistic):                    1.06e-56
Time:                        19:10:26   Log-Likelihood:                         -546.52
No. Observations:                 100   AIC:                                      1095.
Df Residuals:                      99   BIC:                                      1098.
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
x1             3.3844      0.099     34.254      0.000       3.188       3.580
==============================================================================
Omnibus:                        1.766   Durbin-Watson:                   1.974
Prob(Omnibus):                  0.414   Jarque-Bera (JB):                1.278
Skew:                           0.061   Prob(JB):                        0.528
Kurtosis:                       3.540   Cond. No.                         1.00
==============================================================================

Notes:
[1] R² is computed without centering (uncentered) since the model does not contain a constant.
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.'''