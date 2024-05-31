# tuple 沒有生成式的語法，但是有類似的方式可以生成，其語法為：
# variable = tuple(value for item in iterable)
# variable：型別為 tuple 的變數。
# value：生成的值。
# item：從迭代物件裡取出的項目。
# iterable：可迭代的物件。


a = tuple(i for i in range(10))
print(a)   # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# put if to filter
a = tuple(i*i for i in range(10) if i > 5)
print(a)   # (36, 49, 64, 81)
