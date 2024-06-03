import datetime

print("======================  a specific date  =========================")
d = datetime.date(2024, 6, 3)
print(d, type(d), sep=', ')     # 2024-06-03, <class 'datetime.date'>

print("======================  today  =========================")
today = datetime.date.today()   # 2024-06-03, <class 'datetime.date'>
print(today, type(today), sep=', ')

print("======================  datetime properties  =========================")
# 取得日期後，可以使用下面幾種常用的方法，進一步取出日期的資訊進行操作。
today = datetime.date(2024, 6, 3)
print(today)                 # 2024-06-03
print(today.year)            # 2024
print(today.month)           # 6
print(today.day)             # 3
print(today.weekday())       # 0    ( 因為是星期一，所以是 0 )
print(today.isoweekday())    # 1    ( 因為是星期二，所以是 1 )
# datetime.IsoCalendarDate(year=2024, week=23, weekday=1)  ( 第三個數字是星期一，所以是 1 )
print(today.isocalendar())
print(today.isoformat())     # 2024-06-03
print(today.ctime())         # Mon Jun  3 00:00:00 2024
# 回傳特定格式字串所表示的時間 ( 詳細可參考 strftime() 和 strptime() )
print(today.strftime('%Y.%m.%d'))    # 2024.06.03

print("======================  datetime properties  =========================")
newDay = today.replace(year=2020)
print(newDay)                # 2020-06-03

print("======================  date diff  =========================")
d1 = datetime.date(2024, 6, 1)
d2 = datetime.date(2024, 6, 7)
print(abs(d1-d2).days)       # 6

print("======================  time  =========================")
thisTime = datetime.time(12, 0, 0, 1)
print(thisTime)   # 12:00:00.000001

# default is UTC-0, use this way to specify time zone
thisTime = datetime.time(14,0,0,1,tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
print(thisTime)    # 14:00:00.000001+08:00