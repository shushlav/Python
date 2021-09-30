
# example of loading and preparing the breast cancer dataset
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
 
from sklearn.preprocessing import OrdinalEncoder
# EXAMPLE FOR ENCODE:
enc = OrdinalEncoder()
X = [['Male', 1], ['Female', 3], ['Female', 2]]
enc.fit(X)
print(enc.categories_)
print(enc.transform([['Female', 3], ['Male', 1]]))
print(X)

# Results: [array(['Female', 'Male'], dtype=object), array([1, 2, 3], dtype=object)]
#array([[0., 2.],
#       [1., 0.]])