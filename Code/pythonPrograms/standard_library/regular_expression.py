import re

# Refer to
# https://steam.oxxostudio.tw/category/python/library/re.html

print("======================  Search | Case insensitive  =========================")
role = re.compile(r'hello', flags=re.I)  # 匹配 hello，不論大小寫
result = role.search('HeLlo World')

# 如果找不到 group 會發生錯誤 ( 沒有匹配就沒有 group )
if result == None:
    print('找不到資料')      # 沒有匹配就印出找不到資料
else:
    print(result.group())  # 有匹配就印出結果 HeLlo

print("======================  Match | Case insensitive  =========================")
# Match 會從頭開始比對
text = 'Hey, HeLlo World'
result = re.match(r'hello', text, flags=re.I)
print(result)            # None
if result == None:
    print('找不到資料')      # 沒有匹配就印出找不到資料
else:
    print(result.group())  # 有匹配就印出結果 HeLlo

print("======================  sub(pattern, repl, string, count)   =========================")
# re.sub(pattern, repl, string, count) 使用後，會找從 string 找出全部匹配的字串，並使用 repl 的字串取代，count 預設 0 表示全部取代，設定次數可指定取代的個數

text = 'HeLlo world, hello yun'
result1 = re.sub(r'hello', 'yun', text, flags=re.I)
result2 = re.sub(r'hello', 'yun', text, count=1, flags=re.I)
print(result1)     # yun world, yun yun
print(result2)     # yun world, hello yun  ( count 設定 1 所以只換了一個 )
