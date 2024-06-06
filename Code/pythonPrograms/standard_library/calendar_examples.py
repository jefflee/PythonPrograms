import calendar
tc = calendar.TextCalendar()

print("======================  Print a specific month  =========================")
tc.setfirstweekday(6)  # 可以設定日曆裡，每個星期的第一天是星期幾 ( 星期一為 0，星期天為 6 )
print(tc.formatmonth(2024, 6))
# or use the below function
# tc.prmonth(2024, 6)

print("======================  Print a specific year  =========================")
# 產生格式化後一個年份的月曆，w 和 l 是顯示的寬高 ( 可不填 )，c 和 m 表示是垂直和水平顯示的列與欄 ( 可不填 )
print(tc.formatyear(2024, c=3, m=4))
# or use the below function
# tc.pryear(2024, c=3, m=4)

print("======================  isleap(year)  =========================")
# 可以判斷某一年是否為閏年，回傳 True 或 False。
print(calendar.isleap(2020))   # True
print(calendar.isleap(2021))   # False
print(calendar.isleap(2022))   # False
print(calendar.isleap(2024))   # True

print("======================  leapdays(y1, y2)  =========================")
# 可以計算 y1 年到 y2 年之間共包含幾個閏年。
print(calendar.leapdays(1920, 2020))   # 25 ( 1920～2020 年間，有 25 個閏年 )

print("======================  weekheader(n)  =========================")
print(calendar.weekheader(1))   # M T W T F S S
print(calendar.weekheader(2))   # Mo Tu We Th Fr Sa Su
print(calendar.weekheader(3))   # Mon Tue Wed Thu Fri Sat Sun

print("======================  monthrange(year, month)   =========================")
print(calendar.monthrange(2024, 6))
# (calendar.SATURDAY, 30)  2024 的 6 月有 30 天，6 月第一天是星期六

print(calendar.monthrange(2024, 7))   # (0, 30)
# (calendar.MONDAY, 31)  2024 的 7 月有 31 天，6 月第一天是星期一

print("======================  day_name、calendar.day_abbr   =========================")
# 回傳星期一到星期天的名稱或縮寫。
print(list(calendar.day_name))
# ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(list(calendar.day_abbr))
# ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

print("======================  day_name、calendar.day_abbr   =========================")
# 回傳 1～12 月的名稱或縮寫 ( 產生後的第一個值會是空值 )。
print(list(calendar.month_name))
# ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(list(calendar.month_abbr))
# ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
