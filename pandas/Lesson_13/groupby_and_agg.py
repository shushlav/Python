import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')

fare_agg = df['fare'].agg(['sum', 'mean'])
print(fare_agg)
'''
sum     28693.949300
mean       32.204208
Name: fare, dtype: float64'''
agg_func_math = {
    'fare':
    ['sum', 'mean', 'median', 'min', 'max', 'std', 'var', 'mad', 'prod']
}
results = df.groupby(['embark_town']).agg(agg_func_math).round(2)
print(results)
'''
                 fare
                  sum   mean median   min     max    std      var    mad           prod
embark_town
Cherbourg    10072.30  59.95  29.70  4.01  512.33  83.91  7041.39  53.02  6.193716e+250
Queenstown    1022.25  13.28   7.75  6.75   90.00  14.19   201.30   7.87   6.458671e+78
Southampton  17439.40  27.08  13.00  0.00  263.00  35.89  1287.95  21.30   0.000000e+00'''
#    use describe to run multiple built-in aggregations at one time:
agg_func_describe = {'fare': ['describe']}
describe_it = df.groupby(['embark_town']).agg(agg_func_describe).round(2)
print(describe_it)
'''                fare
            describe
               count   mean    std   min    25%    50%   75%     max
embark_town
Cherbourg      168.0  59.95  83.91  4.01  13.70  29.70  78.5  512.33
Queenstown      77.0  13.28  14.19  6.75   7.75   7.75  15.5   90.00
Southampton    644.0  27.08  35.89  0.00   8.05  13.00  27.9  263.00'''
#                       Counting
agg_func_count = {'embark_town': ['count', 'nunique', 'size']}    #count will not include NaN values whereas size will!!
counting = df.groupby(['deck']).agg(agg_func_count)
print(counting)
'''
    embark_town
           count nunique size
deck
A             15       2   15
B             45       2   47
C             59       3   59
D             33       2   33
E             32       3   32
F             13       3   13
G              4       1    4'''
max_rows = df.loc[df.groupby('class')['fare'].idxmax()]
print(max_rows)
'''
     survived  pclass     sex   age  sibsp  parch      fare embarked   class    who  adult_male deck  embark_town alive  alone
258         1       1  female  35.0      0      0  512.3292        C   First  woman       False  NaN    Cherbourg   yes   True
72          0       2    male  21.0      0      0   73.5000        S  Second    man        True  NaN  Southampton    no   True
159         0       3    male   NaN      8      2   69.5500        S   Third    man        True  NaN  Southampton    no  False'''


df1 = pd.DataFrame({'A': 'a a b'.split(), 'B': [1,2,3], 'C': [4,6, 5]})
g = df1.groupby('A')
ap = g.apply(lambda x: x / x.sum())
print(ap)


