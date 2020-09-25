import datetime
#dir(datetime)
#help(datetime.date)

gvr = datetime.date(1956, 1, 31)
print(gvr)    # 1956-01-31
print(gvr.year)  #1956
#   Using timedelta 
mill = datetime.date(2000, 1, 1)    
dt = datetime.timedelta(100)     # adding 100 days (using '-' will dicrease days)
print(mill + dt)  # 2000-04-10


# specify a different display format:
print(gvr.strftime("%A, %B, %d, %Y"))    # Tuesday, January, 31, 1956
message = "GVR was born on {:%A, %B, %d, %Y}."
print(message.format(gvr))   # GVR was born on Tuesday, January, 31, 1956.

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)   # H,M,S
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)

print(launch_date)      # 2017-03-30
print(launch_time)      # 22:27:00
print(launch_datetime)  # 2017-03-30 22:27:00
print(launch_time.minute) # 27
print(launch_datetime.day) # 30
 
 # Current datetime:
now = datetime.datetime.now()   # 2020-09-24 20:56:07.345832
today = datetime.datetime.today()
print(now)
print(today)

# convert a strint to datetime using strptime()

moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)   # 1969-07-20 00:00:00

