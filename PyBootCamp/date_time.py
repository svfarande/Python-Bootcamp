import datetime

my_time = datetime.time(15, 46, 53, 999999)  # ValueError: microsecond must be in 0..999999
print(f"{my_time.hour}H : {my_time.minute}M : {my_time.second}S ({my_time.microsecond}MS)")
# 15H : 46M : 53S (999999MS)
print(my_time)  # 15:46:53.999999

today = datetime.date.today()
print(today)    # 2021-02-14
print(f"{today.day}/{today.month}/{today.year} ({today.isoweekday()})") # 14/2/2021 (7)

date_time = datetime.datetime(2021, 12, 6, 14, 36, 45, 986)
print(date_time)    # 2021-12-06 14:36:45.000986
print(date_time.replace(day=26))  # original object stays unchanged # 2021-12-26 14:36:45.000986
print(date_time)    # 2021-12-06 14:36:45.000986
date_time = date_time.replace(day=26)
print(f"{date_time} ({date_time.timestamp()}) ({date_time.ctime()})")
# 2021-12-26 14:36:45.000986 (1640509605.000986) (Sun Dec 26 14:36:45 2021)

dt1 = datetime.datetime(2021, 11, 26, 15)
dt2 = datetime.datetime(2022, 11, 26, 16)

diff = dt2 - dt1
print(diff) # 365 days, 1:00:00
