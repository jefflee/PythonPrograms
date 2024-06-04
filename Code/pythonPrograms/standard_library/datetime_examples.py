import datetime

print("======================  A specific date  =========================")
d = datetime.date(2024, 6, 3)
print(d, type(d), sep=', ')     # 2024-06-03, <class 'datetime.date'>

print("======================  Today  =========================")
today = datetime.date.today()   # 2024-06-03, <class 'datetime.date'>
print(today, type(today), sep=', ')

print("======================  Date properties  =========================")
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

print("======================  Modify year  =========================")
newDay = today.replace(year=2020)
print(newDay)                # 2020-06-03

print("======================  Date diff  =========================")
d1 = datetime.date(2024, 6, 1)
d2 = datetime.date(2024, 6, 7)
print(abs(d1-d2).days)       # 6

print("======================  Time  =========================")
thisTime = datetime.time(12, 0, 0, 1)
print(thisTime)   # 12:00:00.000001

# default is UTC-0, use this way to specify time zone
thisTime = datetime.time(
    14, 0, 0, 1, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
print(thisTime)    # 14:00:00.000001+08:00

print("======================  Time properties  =========================")
thisTime = datetime.time(
    14, 0, 0, 1, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
print(thisTime)               # 14:00:00.000001+08:00
print(thisTime.isoformat())   # 14:00:00.000001+08:00
print(thisTime.tzname())      # UTC+08:00
print(thisTime.strftime('%H:%M:%S'))   # 14:00:00

print("======================  Modify hour  =========================")
newTime = thisTime.replace(hour=20)
print(newTime)                # 20:00:00.000001+08:00

print("======================  Datetime  =========================")
thisTime = datetime.datetime(2024, 6, 3, 20, 20, 20, 20)
# 2024-06-03 20:20:20.000020, <class 'datetime.datetime'>
print(thisTime, type(thisTime), sep=', ')

print("======================  Today, now, utcnow  =========================")
print(datetime.datetime.today())    # 2024-06-04 18:17:08.628493
# 2024-06-04 18:17:08.628492+08:00
print(datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))))
print(datetime.datetime.now(datetime.UTC))  # 2024-06-04 10:17:08.628492+00:00

print("======================  Datetime detail  =========================")
#  datetime.datetime 將字串轉換為日期時間物件後，就能透過下面幾種常用的方法，將取出的日期時間資訊進行下一步操作。

now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
print(now)                # 2024-06-04 18:19:14.510182+08:00
print(now.date())         # 2024-06-04
print(now.time())         # 18:19:14.510182
print(now.tzname())       # UTC+08:00
print(now.weekday())      # 1
print(now.isoweekday())   # 2
# datetime.IsoCalendarDate(year=2024, week=23, weekday=2)
print(now.isocalendar())
print(now.isoformat())    # 2024-06-04T18:19:14.510182+08:00
print(now.ctime())        # Tue Jun  4 18:19:14 2024
print(now.strftime('%Y/%m/%d %H:%M:%S'))  # 2024/06/04 18:19:14
# time.struct_time(tm_year=2024, tm_mon=6, tm_mday=4, tm_hour=18, tm_min=19, tm_sec=14, tm_wday=1, tm_yday=156, tm_isdst=-1)
print(now.timetuple())

print("======================  Timedelta  =========================")
# 如果要進行日期或時間的計算，可以透過 datetime.timedelta 增加或減少日期或時間，
# 本身包含 days、seconds、microseconds、milliseconds、minutes、hours、weeks 的屬性，屬性的預設值都是 0。
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
nextweek = today + datetime.timedelta(weeks=1)
print(today)       # 2024-06-04 18:22:41.286659
print(yesterday)   # 2024-06-03 18:22:41.286659
print(tomorrow)    # 2024-06-05 18:22:41.286659
print(nextweek)    # 2024-06-11 18:22:41.286659

print("======================  Timezone  =========================")
tzone = datetime.timezone(datetime.timedelta(hours=8))
now = datetime.datetime.now(tz=tzone)
print(now)    # 2024-06-04 18:24:12.937822+08:00
