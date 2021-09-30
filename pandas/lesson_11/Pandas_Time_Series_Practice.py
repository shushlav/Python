# Pandas Time Series Practice
# https://www.w3resource.com/python-exercises/pandas/time-series/index.php

import pandas as pd 
import numpy as np 
import datetime
from datetime import datetime
from pandas.core.indexes.datetimes import date_range

from pandas.core.tools.datetimes import to_datetime
# Write a Pandas program to create Datetime object for Jan 15 2012
print("Datetime object for Jan 11 2012:")
print(datetime(2012, 1, 11))                 # 2012-01-11 00:00:00
# Specific date and time of 9:20 pm.
print(datetime(2012, 1, 11,hour=21, minute=20 ))     #2012-01-11 21:20:00 
print("\nLocal date and time:")
print(datetime.now())                               #2021-06-20 11:44:34.123087
print("\nA date without time:")
print(datetime.date(datetime(2012, 5, 22)))         # 2012-05-22
print("\nCurrent date:")
print(datetime.now().date())                        # 2021-06-20
print("\nTime from a datetime:")
print(datetime.time(datetime(2012, 12, 15, 18, 12)))   # date is mandatory  18:12:00
print("\nCurrent local time:") 
print(datetime.now().time())                            # 11:50:33.114446


# Write a Pandas program to create :a specific date using timestamp
print(pd.Timestamp('2021-01-05'))                       #2021-01-05 00:00:00
print(pd.Timestamp('2021-01-05   11:53'))               # 2021-01-05 11:53:00
print(pd.Timestamp.now())                               # 2021-06-20 11:52:09.407928
print("\nA time adds in the current local date using timestamp:")
print(pd.Timestamp('11:30'))
print("\nCurrent date and time using timestamp:")
print(pd.Timestamp("now"))                              #2021-06-20 11:56:22.583350

# Write a Pandas program to create a date from a given year, month, day and another date from a given string formats.
date1 = pd.Timestamp('2020-08-25')
print ('Current date/time: {}'.format(datetime.now()))      # Current date/time: 2021-06-20 12:00:00.223537

# Write a Pandas program to print the day after and before a specified date. Also print the days between two given dates

def after_before(x):
    print("Current date:", x)
    before = x-pd.Timedelta(days=1)
    print('The day before:', before)
    after = x+pd.Timedelta(days=1)
    print('The day after:', after)
after_before(pd.Timestamp('2021-01-05'))

#print the days between two given dates:
date1 = datetime(2016, 8, 2)
date2 = datetime(2016, 7, 19)
print("\nDifference between two dates: ",(date1 - date2))

#Write a Pandas program to create a time-series with two index labels and random values. Also print the type of the index
dates = [datetime(2011, 9, 1), datetime(2011, 9, 2)]
print("Time-series with two index labels:")
time_series = pd.Series(np.random.randn(2), dates)
print(time_series)
print("\nType of the index:")
print(type(time_series.index))
'''
Time-series with two index labels:
2011-09-01   -0.994802
2011-09-02    1.871923
dtype: float64'''
# Type of the index:
#<class 'pandas.core.indexes.datetimes.DatetimeIndex'>

# Write a Pandas program to create a time-series from a given list of dates as strings
date_list = ['2015-01-02', '2020-03-06', '2018-09-08']
ts = pd.Series(to_datetime(date_list))
print(ts)

'''
0   2015-01-02
1   2020-03-06
2   2018-09-08
dtype: datetime64[ns]'''


# Write a Pandas program to create a time series object that has time indexed data. 
# Also select the dates of same year and select the dates between certain dates
index = pd.DatetimeIndex(date_range('2011-11-01', '2016-06-06', periods=10))  #date range using a startpoint date and a number of periods
ds = pd.Series([1,2,3,4,5,6,7,8,9,10], index= index)
print("Time series object with indexed data:")
print(ds)
'''Time series object with indexed data:
2011-11-01 00:00:00     1
2012-05-05 13:20:00     2
2012-11-08 02:40:00     3
2013-05-13 16:00:00     4
2013-11-16 05:20:00     5
2014-05-21 18:40:00     6
2014-11-24 08:00:00     7
2015-05-29 21:20:00     8
2015-12-02 10:40:00     9
2016-06-06 00:00:00    10
dtype: int64
'''
print("\nDates of same year:")
print(ds['2015'])
print("\nDates between 2012-01-01 and 2012-12-31")
print(ds['2012-01-01':'2012-12-31']) 
'''
Dates of same year:
2015-05-29 21:20:00    8
2015-12-02 10:40:00    9
dtype: int64

Dates between 2012-01-01 and 2012-12-31
2012-05-05 13:20:00    2
2012-11-08 02:40:00    3
dtype: int64
'''
# Write a Pandas program to create a whole month of dates in daily frequencies. Also find the maximum, minimum timestamp and indexs

month = pd.DataFrame(date_range('2021-01-01', '2021-01-31'))
print(month)
print('min: ', month.min())                 # min:  0   2021-01-01
print('max: ', month.max())                 # max:  0   2021-01-31
print("Maximum index: ", month.idxmax())    # Maximum index:  0    30
print("Minimum index: ", month.idxmin())    # Minimum index:  0    0

# Write a Pandas program to create a time series using three months frequency
time_series = pd.date_range('1/1/2021', periods = 36, freq='3M')
print(time_series)
'''
DatetimeIndex(['2021-01-31', '2021-04-30', '2021-07-31', '2021-10-31',
               '2022-01-31', '2022-04-30', '2022-07-31', '2022-10-31',
               '2023-01-31', '2023-04-30', '2023-07-31', '2023-10-31',
               '2024-01-31', '2024-04-30', '2024-07-31', '2024-10-31',
               '2025-01-31', '2025-04-30', '2025-07-31', '2025-10-31',
               '2026-01-31', '2026-04-30', '2026-07-31', '2026-10-31',
               '2027-01-31', '2027-04-30', '2027-07-31', '2027-10-31',
               '2028-01-31', '2028-04-30', '2028-07-31', '2028-10-31',
               '2029-01-31', '2029-04-30', '2029-07-31', '2029-10-31'],
              dtype='datetime64[ns]', freq='3M')
              '''
# Write a Pandas program to create a sequence of durations increasing by an hour
time_series = pd.date_range('1/1/2021 05:00', periods = 10, freq='1H')
print("Hourly range of  10 periods:")
print(time_series)

# Write a Pandas program to convert year and day of year into a single datetime column of a dataframe
data = {\
"year": [2002, 2003, 2015, 2018],
"day_of_the_year": [250, 365, 1, 140]
}
df = pd.DataFrame(data)
print(df)
df["combined"] = df["year"]*1000 + df["day_of_the_year"]      # convert to 7 digits
df["date"] = pd.to_datetime(df["combined"], format = "%Y%j")  # format it to a date
print("\nNew DataFrame:")
print(df)
'''
New DataFrame:
   year  day_of_the_year  combined       date
0  2002              250   2002250 2002-09-07
1  2003              365   2003365 2003-12-31
2  2015                1   2015001 2015-01-01
3  2018              140   2018140 2018-05-20'''

# Write a Pandas program to create a series of Timestamps from a DataFrame of integer or string columns. 
# Also create a series of Timestamps using specified columns.
import pandas as pd
df = pd.DataFrame({'year': [2018, 2019, 2020],
                   'month': [2, 3, 4],
                   'day': [4, 5, 6],
                   'hour': [2, 3, 4]})
print("Original dataframe:")
print(df)
result = pd.to_datetime(df)
print("\nSeries of Timestamps from the said dataframe:")
print(result)
print("\nSeries of Timestamps using specified columns:")
print(pd.to_datetime(df[['year', 'month', 'day']]))
'''
Original dataframe:
   year  month  day  hour
0  2018      2    4     2
1  2019      3    5     3
2  2020      4    6     4

Series of Timestamps from the said dataframe:
0   2018-02-04 02:00:00
1   2019-03-05 03:00:00
2   2020-04-06 04:00:00
dtype: datetime64[ns]

Series of Timestamps using specified columns:
0   2018-02-04
1   2019-03-05
2   2020-04-06'''
# Write a Pandas program to check if a day is a business day (weekday) or not. = pandas.bdate_range
def is_business_day(date):
    return bool(len(pd.bdate_range(date, date)))
print("Check busines day or not?")
print('2020-12-01: ',is_business_day('2020-12-01'))
print('2020-12-06: ',is_business_day('2020-12-06'))
print('2020-12-07: ',is_business_day('2020-12-07'))
print('2020-12-08: ',is_business_day('2020-12-08'))
'''
Check busines day or not?
2020-12-01:  True
2020-12-06:  False
2020-12-07:  True
2020-12-08:  True'''
# Write a Pandas program to get a time series with the last working days of each month of a specific year.
s = pd.date_range('2021-01-01', periods=12, freq='BM')    # 'BM' = business month end frequency
df = pd.DataFrame(s, columns=['Date'])
print('last working days of each month of a specific year:')
print(df.tail())
'''
last working days of each month of a specific year:
         Date
7  2021-08-31
8  2021-09-30
9  2021-10-29
10 2021-11-30
11 2021-12-31'''
# Write a Pandas program to create a time series combining hour and minute.
result = pd.timedelta_range(0, periods=30, freq="1H20T")    # every 1:20
print("For a frequency of 1 hours 20 minutes, here we have combined the hour (H) and minute (T):\n")
print(result)

#Write a Pandas program to convert unix/epoch time to a regular time stamp in UTC. 
# Also convert the said timestamp in to a given time zone.
epoch_t = 1621132355
time_stamp = pd.to_datetime(epoch_t, unit='s')
# UTC (Coordinated Universal Time) is one of the well-known names of UTC+0 time zone which is 0h.
# By default, time series objects of pandas do not have an assigned time zone.
print("Regular time stamp in UTC:")
print(time_stamp)
print("\nConvert the said timestamp in to US/Pacific:")
print(time_stamp.tz_localize('UTC').tz_convert('US/Pacific'))
print("\nConvert the said timestamp in to Europe/Berlin:")
print(time_stamp.tz_localize('UTC').tz_convert('Europe/Berlin'))
'''
Regular time stamp in UTC:
2021-05-16 02:32:35

Convert the said timestamp in to US/Pacific:
2021-05-15 19:32:35-07:00

Convert the said timestamp in to Europe/Berlin:
2021-05-16 04:32:35+02:00'''

# Write a Pandas program to calculate all Thursdays between two given days
thursdays  = pd.date_range('2020-01-01', 
                           '2020-12-31', freq="W-THU")
print("All Thursdays between 2020-01-01 and 2020-12-31:\n")
print(thursdays.values)


