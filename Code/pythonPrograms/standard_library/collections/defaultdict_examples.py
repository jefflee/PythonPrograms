from collections import defaultdict

a = 'hello world'
b = defaultdict(lambda: 0)   # 創建一個空的使用預設值 0 的 dict 物件
for i in a:
    b[i] += 1    # 依序將 a 的字母設為 key，如果有 key 就將數值增加 1
# defaultdict(<function <lambda> at 0x10d7d5290>, {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
print(b)

c = defaultdict(lambda: 'no')   # 如果 key 不存在，就回傳 no
for i in a:
    c[i] = i      # 依序將 a 的字母設為 key 和值
print(c['h'])   # h
print(c['a'])   # no
