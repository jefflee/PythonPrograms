from collections import Counter
# Counter 可以創建一個 dict 計數器物件，用來計算可迭代物件中每個物件的數量

t1 = 'hello world'
a = Counter(t1)     # 創建一個計數器物件
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
print(a)

b = list(a.elements())   # 取出每個項目成為串列
# ['h', 'e', 'l', 'l', 'l', 'o', 'o', ' ', 'w', 'r', 'd']
print(b)
# 排序 [' ', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
print(sorted(b))

c = a.most_common(3)     # 取出前三多的項目
print(c)                 # [('l', 3), ('o', 2), ('h', 1)]

t2 = 'hello'
e = Counter(t2)          # 建立新的計數器物件
a.update(e)              # 加上新物件中的數量
# Counter({'l': 5, 'o': 3, 'h': 2, 'e': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
print(a)
a.subtract(e)            # 減去新物件中的數量
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
print(a)
