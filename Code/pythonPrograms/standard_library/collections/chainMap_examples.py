from collections import ChainMap
# ChainMap 可以創建一個類似 dict 的物件，可以將多個 dict 串接成單一的物件，
# 串接後只要讀取指定的屬性，就能取得對應的內容 ( 屬性相同的會取第一個屬性 )

a = {'x': 1, 'y': 2}
b = {'m': 3, 'n': 4}
c = {'i': 5, 'j': 6}
d = ChainMap(a, b, c)    # 根據 a、b、c 建立一個 ChainMap 物件
print(d['m'], d['j'])    # 3 6 讀取 ChainMap 物件中的 'm' 和 'j'
# [{'x': 1, 'y': 2}, {'m': 3, 'n': 4}, {'i': 5, 'j': 6}]
print(d.maps)
print(d.maps[0])         # {'x': 1, 'y': 2}

e = d.new_child()           # 加入一個空 dict 成為新的 ChainMap 物件
# ChainMap({}, {'x': 1, 'y': 2}, {'m': 3, 'n': 4}, {'i': 5, 'j': 6})
print(e)
f = d.new_child({'z': 100})  # 加入一個 'z':100} 成為新的 ChainMap 物件
# ChainMap({'z': 100}, {'x': 1, 'y': 2}, {'m': 3, 'n': 4}, {'i': 5, 'j': 6})
print(f)
g = d.parents     # 去除第一個項目，成為新的 ChainMap 物件
h = g.parents     # 去除第一個項目，成為新的 ChainMap 物件
print(g)          # ChainMap({'m': 3, 'n': 4}, {'i': 5, 'j': 6})
print(h)          # ChainMap({'i': 5, 'j': 6})
