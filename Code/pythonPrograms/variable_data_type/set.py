print("======================  Create a set or Convert to set  =========================")
a = set()
b = set([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
c = set({'x': 1, 'y': 2, 'z': 3})
d = set('hello')
print(a)   # set()
print(b)   # {1, 2, 3, 4, 5}  只留下不重複的部分
print(c)   # {'x', 'y', 'z'}  如果是字典，只保留鍵
print(d)   # {'l', 'o', 'h', 'e'}  只留下不重複的部分

a = {0, 1, 2, 3, 'a', 'b', False}
print(a)  # {0, 1, 2, 3, 'a', 'b'}  False 等同於 0，所以只保留 0

print("======================  Add an item  =========================")
a = {0, 1, 2, 3, 4, 5}
a.add('x')
a.add('y')
print(a)   # {0, 1, 2, 3, 4, 5, 'x', 'y'}

print("======================  Remove an item / Discard an item =========================")
a = {0, 1, 2, 3, 'x', 'y', 'z', '1'}
a.remove('x')
print(a)   # {0, 1, 2, 3, 'y', 'z', '1'}

a = {0, 1, 2, 3, 'x', 'y', 'z'}
a.discard('x')
a.discard('a')   # 不會發生錯誤
print(a)         # {0, 1, 2, 3, 'y', 'z'}

print("======================  Intersection, union, difference, symmetric_difference =========================")
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

# 交集
print(a.intersection(b))   # {3, 4, 5}
print(a & b)                 # {3, 4, 5}
# 聯集
print(a.union(b))          # {1, 2, 3, 4, 5, 6, 7}
print(a | b)                 # {1, 2, 3, 4, 5, 6, 7}
# 差集
print(a.difference(b))     # {1, 2}
print(a-b)                 # {1, 2}
# 對稱差集
print(a.symmetric_difference(b))  # {1, 2, 6, 7}
print(a ^ b)                        # {1, 2, 6, 7}

print("======================  Subset or superset  =========================")
a = {1, 2, 3, 4, 5, 6, 7}
b = {3, 4, 5, 6, 7}
c = {1, 2, 3, 4, 5, 6, 7}
d = {6, 7, 8, 9}

print(a <= a)   # True 自己是自己的子集合
print(b <= a)   # True b 是 a 的子集合
print(b < a)    # True b 也是 a 的真子集合 ( 因爲沒有等於，完全包含 )
print(c <= a)   # True c 是 a 的子集合
print(a <= c)   # True a 也是 c 的子集合
print(d < a)    # False d 和 a 沒有子集合或超集合關係

print("======================  issubset / issuperset  =========================")
a = {1, 2, 3, 4, 5, 6, 7}
b = {3, 4, 5, 6, 7}
c = {1, 2, 3, 4, 5, 6, 7}
d = {6, 7, 8, 9}

print(b.issubset(a))     # True b 是 a 的子集合
print(a.issuperset(b))   # True a 是 b 的超集合
print(c.issubset(a))     # True c 是 a 的子集合
print(d.issubset(a))     # Fasle d 不是 a 的子集合

print("======================  Exist  =========================")
a = {'a', 'b', 'c', 'd', 1, 2, 3}
print('b' in a)    # True
print(2 in a)      # True
print(99 in a)     # False
