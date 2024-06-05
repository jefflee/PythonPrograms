import time

print("======================  time()  =========================")
# time.time() 執行後會回傳 1970 年 1 月 1 日 00:00:00 到現在的秒數 ( 精確度到 1/1000000 秒 )，秒數使用浮點數 float 的格式
print(time.time())     # 1717549640.0178862
# time.time_ns() 會回傳 ns 數 ( 1/1000000000 秒 )
print(time.time_ns())  # 1717549640017886300


print("======================  sleep(sec)  =========================")
print(time.ctime(time.time()))   # Wed Jun  5 09:07:20 2024
time.sleep(2)                    # 暫停兩秒
print(time.ctime(time.time()))   # Wed Jun  5 09:07:22 2024

print("======================  ctime(t)  =========================")
# time.ctime(t) 能將 time.time(t) 得到的時間，轉換為本地時間。
t = time.time()
print(time.ctime(t))   # Wed Jun  5 09:07:22 2024

print("======================  asctime()  =========================")
t = time.time()
t1 = time.localtime(t)
t2 = time.asctime(t1)
print(t)      # 1717549642.0197787
print(t1)     # time.struct_time(tm_year=2024, tm_mon=6, tm_mday=5, tm_hour=9, tm_min=7, tm_sec=22, tm_wday=2, tm_yday=157, tm_isdst=0)
print(t2)     # Wed Jun  5 09:07:22 2024

print("======================  strftime(t)、time.strptime(t)   =========================")
# time.strftime(t) 可以將時間轉換為特定格式字串
# time.strptime(t) 則會將特定格式的字串，轉換為 struct_time 格式的時間

t = time.time()
t1 = time.localtime(t)
t2 = time.strftime('%Y/%m/%d %H:%M:%S', t1)
t3 = time.strptime(t2, '%Y/%m/%d %H:%M:%S')
print(t)     # 1717549642.0197787
print(t1)    # time.struct_time(tm_year=2024, tm_mon=6, tm_mday=5, tm_hour=9, tm_min=7, tm_sec=22, tm_wday=2, tm_yday=157, tm_isdst=0)
print(t2)    # 2024/06/05 09:07:22
print(t3)    # time.struct_time(tm_year=2024, tm_mon=6, tm_mday=5, tm_hour=9, tm_min=7, tm_sec=22, tm_wday=2, tm_yday=157, tm_isdst=-1)
