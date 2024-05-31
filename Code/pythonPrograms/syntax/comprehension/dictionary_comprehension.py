# result = {key: value for item in iterable}
# result：生成的新字典。
# key：生成的鍵。
# value：生成的值。
# item：從迭代物件裡取出的項目。
# iterable：可迭代的物件。

print('=======================  basic  ==============================')
a = {i: i*i for i in range(1, 10)}
print(a)       # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}7
