# result = {value for item in iterable}
# result：生成的新集合。
# value：生成的值。
# item：從迭代物件裡取出的項目。
# iterable：可迭代的物件。

print('=======================  basic  ==============================')
a = {i*i for i in range(1, 10)}
print(a)       # {64, 1, 4, 36, 9, 16, 49, 81, 25}
