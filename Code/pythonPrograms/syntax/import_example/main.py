import datetime
from datetime import date # import and use alias
import ok
from subfolder import ok2

ok.talk('hi')   # hi
ok2.talk('ok2') # ok2

print(datetime.datetime.now())   # 2024-05-31 15:44:52.149074
print(datetime.date.today())     # 2024-05-31

print(date.today())     # 2024-05-31