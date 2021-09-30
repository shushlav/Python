# Group by

# importing pandas as pd
import pandas as pd
  
# Creating the dataframe 
df = pd.read_csv("nba.csv")
  
# Print the dataframe
print(df.head())

# applying groupby() function to group the data on 'team' value.
gk = df.groupby('Team')
  
# Let's print the first entries in all the groups formed.
print(gk.first())

# Finding the values contained in the "Boston Celtics" group
print(gk.get_group('Boston Celtics'))
'''
               Name            Team  Number Position   Age Height  Weight            College      Salary
0     Avery Bradley  Boston Celtics     0.0       PG  25.0    6-2   180.0              Texas   7730337.0
1       Jae Crowder  Boston Celtics    99.0       SF  25.0    6-6   235.0          Marquette   6796117.0
2      John Holland  Boston Celtics    30.0       SG  27.0    6-5   205.0  Boston University         NaN
3       R.J. Hunter  Boston Celtics    28.0       SG  22.0    6-5   185.0      Georgia State   1148640.0
4     Jonas Jerebko  Boston Celtics     8.0       PF  29.0   6-10   231.0                NaN   5000000.0
5      Amir Johnson  Boston Celtics    90.0       PF  29.0    6-9   240.0                NaN  12000000.0
6     Jordan Mickey  Boston Celtics    55.0       PF  21.0    6-8   235.0                LSU   1170960.0
7      Kelly Olynyk  Boston Celtics    41.0        C  25.0    7-0   238.0            Gonzaga   2165160.0
8      Terry Rozier  Boston Celtics    12.0       PG  22.0    6-2   190.0         Louisville   1824360.0
9      Marcus Smart  Boston Celtics    36.0       PG  22.0    6-4   220.0     Oklahoma State   3431040.0
10  Jared Sullinger  Boston Celtics     7.0        C  24.0    6-9   260.0         Ohio State   2569260.0
11    Isaiah Thomas  Boston Celtics     4.0       PG  27.0    5-9   185.0         Washington   6912869.0
12      Evan Turner  Boston Celtics    11.0       SG  27.0    6-7   220.0         Ohio State   3425510.0
13      James Young  Boston Celtics    13.0       SG  20.0    6-6   215.0           Kentucky   1749840.0
14     Tyler Zeller  Boston Celtics    44.0        C  26.0    7-0   253.0     North Carolina   2616975.0
'''
# Use groupby() function to form groups based on more than one category 
# (i.e. Use more than one column to perform the splitting).

gkk = df.groupby(['Team', 'Position'])
print(gkk.first())
'''
                                        Name  Number   Age Height  Weight               College      Salary
Team               Position
Atlanta Hawks      C               Al Horford    15.0  30.0   6-10   245.0               Florida  12000000.0
                   PF          Kris Humphries    43.0  31.0    6-9   235.0             Minnesota   1000000.0
                   PG         Dennis Schroder    17.0  22.0    6-1   172.0           Wake Forest   1763400.0
                   SF           Kent Bazemore    24.0  26.0    6-5   201.0          Old Dominion   2000000.0
                   SG        Tim Hardaway Jr.    10.0  24.0    6-6   205.0              Michigan   1304520.0
...                                       ...     ...   ...    ...     ...                   ...         ...
Washington Wizards C            Marcin Gortat    13.0  32.0   6-11   240.0  North Carolina State  11217391.0
                   PF             Drew Gooden    90.0  34.0   6-10   250.0                Kansas   3300000.0
                   PG          Ramon Sessions     7.0  30.0    6-3   190.0                Nevada   2170465.0
                   SF            Jared Dudley     1.0  30.0    6-7   225.0        Boston College   4375000.0
                   SG           Alan Anderson     6.0  33.0    6-6   220.0        Michigan State   4000000.0'''

print(gkk.agg({'Salary': ['mean'], 'Age': ['max', 'mean', 'count']}))
'''
                                   Salary   Age
                                     mean   max       mean count
Team               Position
Atlanta Hawks      C         7.585417e+06  31.0  28.333333     3
                   PF        5.988067e+06  31.0  28.250000     4
                   PG        4.881700e+06  27.0  24.500000     2
                   SF        3.000000e+06  32.0  29.000000     2
                   SG        2.607758e+06  35.0  29.500000     4
...                                   ...   ...        ...   ...
Washington Wizards C         8.163476e+06  33.0  30.666667     3
                   PF        5.650000e+06  34.0  30.000000     2
                   PG        9.011208e+06  30.0  27.500000     2
                   SF        2.789700e+06  30.0  25.500000     4
                   SG        2.839248e+06  33.0  27.250000     4

[149 rows x 4 columns]'''

#   Iterating through groups:
for name, group in gk:
    print(name)
    print(group)
'''
Atlanta Hawks
                 Name           Team  Number Position   Age Height  Weight         College      Salary
309     Kent Bazemore  Atlanta Hawks    24.0       SF  26.0    6-5   201.0    Old Dominion   2000000.0
310  Tim Hardaway Jr.  Atlanta Hawks    10.0       SG  24.0    6-6   205.0        Michigan   1304520.0
311      Kirk Hinrich  Atlanta Hawks    12.0       SG  35.0    6-4   190.0          Kansas   2854940.0
312        Al Horford  Atlanta Hawks    15.0        C  30.0   6-10   245.0         Florida  12000000.0
313    Kris Humphries  Atlanta Hawks    43.0       PF  31.0    6-9   235.0       Minnesota   1000000.0
314       Kyle Korver  Atlanta Hawks    26.0       SG  35.0    6-7   212.0       Creighton   5746479.0
315      Paul Millsap  Atlanta Hawks     4.0       PF  31.0    6-8   246.0  Louisiana Tech  18671659.0
316      Mike Muscala  Atlanta Hawks    31.0       PF  24.0   6-11   240.0        Bucknell    947276.0
317   Lamar Patterson  Atlanta Hawks    13.0       SG  24.0    6-5   225.0      Pittsburgh    525093.0
318   Dennis Schroder  Atlanta Hawks    17.0       PG  22.0    6-1   172.0             NaN   1763400.0
319        Mike Scott  Atlanta Hawks    32.0       PF  27.0    6-8   237.0        Virginia   3333333.0
320   Thabo Sefolosha  Atlanta Hawks    25.0       SF  32.0    6-7   220.0             NaN   4000000.0
321    Tiago Splitter  Atlanta Hawks    11.0        C  31.0   6-11   245.0             NaN   9756250.0
322    Walter Tavares  Atlanta Hawks    22.0        C  24.0    7-3   260.0             NaN   1000000.0
323       Jeff Teague  Atlanta Hawks     0.0       PG  27.0    6-2   186.0     Wake Forest   8000000.0
Boston Celtics
               Name            Team  Number Position   Age Height  Weight            College      Salary
0     Avery Bradley  Boston Celtics     0.0       PG  25.0    6-2   180.0              Texas   7730337.0
1       Jae Crowder  Boston Celtics    99.0       SF  25.0    6-6   235.0          Marquette   6796117.0
2      John Holland  Boston Celtics    30.0       SG  27.0    6-5   205.0  Boston University         NaN
3       R.J. Hunter  Boston Celtics    28.0       SG  22.0    6-5   185.0      Georgia State   1148640.0
4     Jonas Jerebko  Boston Celtics     8.0       PF  29.0   6-10   231.0                NaN   5000000.0
5      Amir Johnson  Boston Celtics    90.0       PF  29.0    6-9   240.0                NaN  12000000.0
6     Jordan Mickey  Boston Celtics    55.0       PF  21.0    6-8   235.0                LSU   1170960.0
7      Kelly Olynyk  Boston Celtics    41.0        C  25.0    7-0   238.0            Gonzaga   2165160.0
8      Terry Rozier  Boston Celtics    12.0       PG  22.0    6-2   190.0         Louisville   1824360.0
9      Marcus Smart  Boston Celtics    36.0       PG  22.0    6-4   220.0     Oklahoma State   3431040.0
10  Jared Sullinger  Boston Celtics     7.0        C  24.0    6-9   260.0         Ohio State   2569260.0
11    Isaiah Thomas  Boston Celtics     4.0       PG  27.0    5-9   185.0         Washington   6912869.0
12      Evan Turner  Boston Celtics    11.0       SG  27.0    6-7   220.0         Ohio State   3425510.0
13      James Young  Boston Celtics    13.0       SG  20.0    6-6   215.0           Kentucky   1749840.0
14     Tyler Zeller  Boston Celtics    44.0        C  26.0    7-0   253.0     North Carolina   2616975.0
....
'''
