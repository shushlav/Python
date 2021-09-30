import pandas as pd
import numpy as np 
data = pd.read_csv('train_ctrUa4K.csv', index_col='Loan_ID')

#Create a new function:
def num_missing(x):
    return sum(x.isnull())

#Applying per column:
print ("Missing values per column:\n")
print (data.apply(num_missing, axis=0)) #axis=0 defines that function is to be applied on each column

# Imputing missing values using Pandas ‘fillna()’ does it in one go. It is used for updating missing values with the overall mean/mode/median of the column. 
#Let’s impute the ‘Gender’, ‘Married’ and ‘Self_Employed’ columns with their respective modes.
#First we import scipy function to determine the mode
from scipy.stats import mode
mode(data['Gender'])
mode(data['Gender']).mode[0]    #We will take the first one by default 
#Impute the values:
data['Gender'].fillna(mode(data['Gender']).mode[0], inplace=True)    # as an example.....will put all missing values as 'male'
data['Married'].fillna(mode(data['Married']).mode[0], inplace=True)
data['Self_Employed'].fillna(mode(data['Self_Employed']).mode[0], inplace=True)

#Now check the #missing values again to confirm:
print (data.apply(num_missing, axis=0))
'''
Missing values per column:

Gender               13
Married               3
Dependents           15
Education             0
Self_Employed        32
ApplicantIncome       0
CoapplicantIncome     0
LoanAmount           22
Loan_Amount_Term     14
Credit_History       50
Property_Area         0
Loan_Status           0
dtype: int64
Gender                0
Married               0
Dependents           15
Education             0
Self_Employed         0
ApplicantIncome       0
CoapplicantIncome     0
LoanAmount           22
Loan_Amount_Term     14
Credit_History       50
Property_Area         0
Loan_Status           0
dtype: int64
'''
#Pivot Table in Pandas to fill missing values to LoanAmount
#Determine pivot table
impute_grps = data.pivot_table(values=["LoanAmount"], index=["Gender","Married","Self_Employed"], aggfunc=np.mean)
print(impute_grps)
print(impute_grps.index)
'''
MultiIndex([('Female',  'No',  'No'),
            ('Female',  'No', 'Yes'),
            ('Female', 'Yes',  'No'),
            ('Female', 'Yes', 'Yes'),
            (  'Male',  'No',  'No'),
            (  'Male',  'No', 'Yes'),
            (  'Male', 'Yes',  'No'),
            (  'Male', 'Yes', 'Yes')],
           names=['Gender', 'Married', 'Self_Employed'])'''

impute_grps.loc[('Male', 'Yes', 'No'), 'LoanAmount']    # 153.8827361563518

#iterate only through rows with missing LoanAmount
for i,row in data.loc[data['LoanAmount'].isnull(),:].iterrows():
    ind = tuple([row['Gender'],row['Married'],row['Self_Employed']])
    data.loc[i,'LoanAmount'] = impute_grps.loc[ind].values[0]

#Now check the #missing values again to confirm:
print(data.apply(num_missing, axis=0))      # LoanAmount            0

#cross-tabulation Test if “Credit_History” is expected to affect the loan status computes a frequency table of the factors
pd.crosstab(data["Credit_History"],data["Loan_Status"],margins=True)    # in absolute numbers
'''
Loan_Status       N    Y  All
Credit_History
0.0              82    7   89
1.0              97  378  475
All             179  385  564
'''
# convert to %:
pd.crosstab(data["Credit_History"],data["Loan_Status"], normalize='index').round(4)*100    
#Normalize  = by dividing all values by the sum of values. 'index' will normalize over each row

# Merge Pandas DataFrames
prop_rates = pd.DataFrame([1000, 5000, 12000], index=['Rural','Semiurban','Urban'],columns=['rates'])
#merge this information with the original Pandas dataframe:
data_merged = data.merge(right=prop_rates, how='inner',left_on='Property_Area',right_index=True, sort=False)
#inner: use intersection of keys from both frames; right: use only keys from right frame
print(data_merged.head())
data_merged.pivot_table(values='Credit_History',index=['Property_Area','rates'], aggfunc=len)
'''
                     Credit_History
Property_Area rates
Rural         1000            179.0
Semiurban     5000            233.0
Urban         12000           202.0'''

# 8 – Sorting Pandas DataFrames
data_sorted = data.sort_values(['ApplicantIncome','CoapplicantIncome'], ascending=False)
print(data_sorted[['ApplicantIncome','CoapplicantIncome']])

#9 – Plotting (Boxplot & Histogram) with Pandas

import matplotlib.pyplot as plt

data.boxplot(column="ApplicantIncome",by="Loan_Status")   # compare the distribution of ApplicantIncome by Loan_Status
plt.show()

data.hist(column="ApplicantIncome",by="Loan_Status",bins=30)
plt.show()
#This shows that income is not a big deciding factor on its own as there is no appreciable difference between 
# the people who received and were denied the loan.

