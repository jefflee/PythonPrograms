# Refer to
# https://steam.oxxostudio.tw/category/python/basic/builtin-iter.html#a6

print("======================  Enumerate(x, start=y)  =========================")
# enumerate() 可以將「串列、集合、tuple、字典」建立為可迭代並附加索引值的 enumerate 物件，
# start 的數值代表索引值開始的數字，預設從 0 開始 ( 不填入預設 0 )。
a = enumerate(['a', 'b', 'c'])
b = enumerate(('a', 'b', 'c'))
c = enumerate({'a', 'b', 'c'})
d = enumerate({'a': 1, 'b': 2, 'c': 3}, start=2)
print(a)          # <enumerate object at 0x7f8de8677050>
print(list(a))    # [(0, 'a'), (1, 'b'), (2, 'c')]
print(list(b))    # [(0, 'a'), (1, 'b'), (2, 'c')]
print(list(c))    # [(0, 'a'), (1, 'b'), (2, 'c')]
print(list(d))    # [(2, 'a'), (3, 'b'), (4, 'c')] 設定 start=2，第一項的索引值變成 2

print("======================  iter(x)  =========================")
# iter() 可以將「串列、集合、tuple、字典」建立為可迭代的 iter 物件，下方程式可以看到不同型態的 iter 物件。
a = iter([1, 2, 3])
b = iter((1, 2, 3))
c = iter({'a', 'b', 'c'})
d = iter({'a': 1, 'b': 2, 'c': 3})
print(a)    # <list_iterator object at 0x7f8de866e450>
print(b)    # <tuple_iterator object at 0x7f8de866ec90>
print(c)    # <set_iterator object at 0x7f8de86c0910>
print(d)    # <dict_keyiterator object at 0x7f8de86ec7d0>

print("======================  next(x)  =========================")
a = enumerate(['a', 'b', 'c'])
print(next(a))    # (0, 'a')
print(next(a))    # (1, 'b')
print(next(a))    # (2, 'c')
print(next(a))
print(list(a))    # []    # 全部取出後只剩下空串列

b = iter(['a', 'b', 'c'])
print(next(b))    # a
print(next(b))    # b
print(next(b))    # c
print(list(b))    # []    # 全部取出後只剩下空串列
