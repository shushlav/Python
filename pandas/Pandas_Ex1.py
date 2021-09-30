'''
Created on Jul 01, 2016

@author: Dar Lador

'''

#(1) import pandas as pd
import pandas as pd



# The lists below hold the recorded data of the last three days.

UserID = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
RegistrationDate = ['07-01-2016', '07-01-2016', '07-01-2016', '06-30-2016', '06-30-2016', '06-29-2016', '06-28-2016', '06-28-2016', '06-28-2016', '06-28-2016']
FirstName = ['Dina', 'Moran', 'Shira', 'Hila', 'Tamar', 'Hagar', 'Michal', 'Osnat', 'Galit', 'Einat']
LastName = ['Marom', 'Cohen', 'Levi', 'Zach', 'Aviv', 'Golan', 'Shamir', 'Jakob', 'Shem-Tov', 'Goldshtein']
Course = ['Android', 'Web', 'Python', 'Python', 'Python', 'Android', 'Python', 'Web', 'Python', 'Web']

df = pd.DataFrame()
df['UserID'] = UserID
df['Course'] = Course
df['FirstName'] = FirstName
df['LastName'] = LastName
df['RegistrationDate'] = RegistrationDate
print(df)





# (2) Using the lists above, try to get this output:
'''
         Course FirstName    LastName RegistrationDate
UserID                                                
1001    Android      Dina       Marom       07-01-2016
1002        Web     Moran       Cohen       07-01-2016
1003     Python     Shira        Levi       07-01-2016
1004     Python      Hila        Zach       06-30-2016
1005     Python     Tamar        Aviv       06-30-2016
1006    Android     Hagar       Golan       06-29-2016
1007     Python    Michal      Shamir       06-28-2016
1008        Web     Osnat       Jakob       06-28-2016
1009     Python     Galit    Shem-Tov       06-28-2016
1010        Web     Einat  Goldshtein       06-28-2016
'''





# (3) Try to get this output:
'''
    Course FirstName LastName RegistrationDate  UserID
0  Android      Dina    Marom       07-01-2016    1001
1      Web     Moran    Cohen       07-01-2016    1002
'''
print(df.head(2))




#(4) Get this output:
'''
         Course FirstName LastName RegistrationDate
UserID                                             
1001    Android      Dina    Marom       07-01-2016
1002        Web     Moran    Cohen       07-01-2016
1003     Python     Shira     Levi       07-01-2016
1004     Python      Hila     Zach       06-30-2016
1005     Python     Tamar     Aviv       06-30-2016
'''
print(df.head())



