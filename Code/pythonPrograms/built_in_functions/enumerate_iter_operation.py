# Refer to
# https://steam.oxxostudio.tw/category/python/basic/builtin-iter-2.html

print("======================  range(start, stop, step)  =========================")
a = range(1, 5)
b = range(1, 100, 10)
c = range(5, -5, -1)
print(list(a))   # [1, 2, 3, 4]
print(list(b))   # [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
print(list(c))   # [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]

print("======================  map(function, iter)  =========================")


def a(x):
    return x+1


b = map(a, [1, 2, 3, 4, 5])
c = map(lambda x: x+1, [1, 2, 3, 4, 5])
d = [i+1 for i in [1, 2, 3, 4, 5]]

print(list(b), type(b))    # [2, 3, 4, 5, 6] <class 'map'>
print(tuple(c), type(c))   # (2, 3, 4, 5, 6) <class 'map'>
print(d, type(d))          # [2, 3, 4, 5, 6] <class 'list'>

# 因為 map 回傳的是一個可迭代物件，所以也可以將其賦值給變數，下方的例子，使用 map 將一個字串的串列內容，分別賦值給 a 和 b 兩個變數。
t = ['12', '34']
a, b = map(int, t)
print(a)    # 12
print(b)    # 34

print("======================  filter(function, iter)  =========================")
# 和上面一樣，也可以利用 comprehension，參考 list_comprehension.py


def a(x):
    return x > 2


b = filter(a, [1, 2, 3, 4, 5])
c = filter(lambda x: x > 2, [1, 2, 3, 4, 5])

print(list(b), type(bin))    # [3, 4, 5] <class 'builtin_function_or_method'>
print(tuple(c), type(c))   # (3, 4, 5) <class 'filter'>

print("======================  sorted(x, key=None, reverse=False)   =========================")
a = [1, 5, 3, 4, 2]
b = sorted(a)
c = sorted(a, reverse=True)

print(list(b))   # [1, 2, 3, 4, 5]
print(list(c))   # [5, 4, 3, 2, 1]

print("======================  sorted(x, key=None, reverse=False) | Example 2  =========================")
# 下方程式的 a 是一個二維的串列，使用 key 來讓排序以第二個項目做為依據，範例中使用具名函式 test 和 lambda 函式，都是一樣的效果
a = [[1, 8], [2, 1], [5, 2], [3, 5], [9, 3]]
b = sorted(a, key=lambda x: x[1])


def test(x):
    return x[1]


c = sorted(a, key=test)

print(list(b))   # [[2, 1], [5, 2], [9, 3], [3, 5], [1, 8]]
print(list(c))   # [[2, 1], [5, 2], [9, 3], [3, 5], [1, 8]]


# reversed() 可以將有順序性的物件 ( 字串、串列和 tuple ) 內容反轉，產生一個全新的物件。

a = [1, 2, 3, 4, 5]
b = (1, 2, 3, 4, 5)
c = '12345'

print(list(reversed(a)))   # [5, 4, 3, 2, 1]
print(list(reversed(b)))   # [5, 4, 3, 2, 1]
print(list(reversed(c)))   # ['5', '4', '3', '2', '1']

d = ''.join(list(reversed(c)))
print(d, type(d))  # 54321 <class 'str'>

print("======================  all(x)  =========================")
# all() 可以判斷一個可迭代物件裡，是否不包含 False 相關的元素
# ( 只要是 0、空白、False 都屬於 False 元素 )，
# 如果不包含或「空物件」就會回傳 True，如果包含就會回傳 False。

a = [1, 2, 3, 4, 5]
b = [0, 1, 2, 3, 4, 5]
c = ['x', 'y', 'z', '']
d = []

print(all(a))    # True
print(all(b))    # False
print(all(c))    # False
print(all(d))    # True

print("======================  any(x)  =========================")
# any() 可以判斷一個可迭代物件裡，是否包含了 True 相關的元素
# ( 只要不是 0、空白、False 都屬於 True 元素 )，
# 如果包含就會回傳 True，反之不包含就會回傳 False，
# 此外，如果是「空」的物件，會回傳 False。

a = [1, 2, 3, 4, 5]
b = [0, 1, 2, 3, 4, 5]
c = ['x', 'y', 'z', '']
d = []

print(any(a))    # True
print(any(b))    # True
print(any(c))    # True
print(any(d))    # False

print("======================  slice(start, stop, step)  =========================")
# slice(start, stop, step) 可以「定義切片範圍」，當指定的可迭代物件套用範圍後，就會取出範圍內的項目，變成新的物件。
a = slice(2, 6)
b = slice(2, 6, 2)
c = [1, 2, 3, 4, 5, 6, 7, 8, 9]

d = c[a]
e = c[b]
print(d)        # [3, 4, 5, 6]
print(c[2:6])   # [3, 4, 5, 6]
print(e)        # [3, 5]

print(c[2:])    # [3, 4, 5, 6, 7, 8, 9]
print(c[2:-1])  # [3, 4, 5, 6, 7, 8]
print(c[:-1])   # [1, 2, 3, 4, 5, 6, 7, 8]
print(c[-1])    # 9

print("======================  zip()  =========================")
# zip() 可以將指定的可迭代物件，打包變成一個新的物件，
# 新物件的長度與「最短」的一致，
# 下方的例子將 a、b、c 三個列表打包，最後使用 list() 轉換成串列。

a = [1, 2, 3, 4]
b = [5, 6, 7]
c = [8, 9]
d = zip(a, b, c)
print(list(d))    # [(1, 5, 8), (2, 6, 9)]
print(list(zip(a, b)))
