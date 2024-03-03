import time

# Create a list that is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr1 = []
for i in range(10):
    arr1.append(i)
print(arr1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use List Comprehension( in-place construction)
arr1 = [i for i in range(10)]
print(arr1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# you can use if to filter the elements
# for x in arr1 意思是迴圈，在迴圈裡要加 if 條件。最前面的 x 是指宣告的 list 的element
arr2 = [x for x in arr1 if x % 2 == 0]
print(arr2)  # [0, 2, 4, 6, 8]

# you can use as many conditions as you want!
arr3 = [x for x in arr1 if x >= 3 and x % 2 == 0]
print(arr3)  # [4, 6, 8]

# use nested for loops to make everyone dizzy XD
arr4 = [(x, y) for x in range(3) for y in range(4)]
print(arr4)  # [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]
print(arr4[0])  # (0, 0)
print(arr4[0][0])  # 0
print(arr4[0][1])  # 0
print(arr4[1])  # (0, 1)
print(arr4[1][0])  # 0
print(arr4[1][1])  # 1

# what if we don't assign comprehension to list?
# list comprehension 背後是 generator class
comp = (i for i in range(10))
print(comp)  # <generator object <genexpr> at 0x0000013BF7306980>
print(type(comp))  # <class 'generator'>

arr1 = list(comp)
arr2 = list(comp)
arr3 = [comp]
print(arr1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr2)  # []
print(arr3)  # [<generator object <genexpr> at 0x0000023484776980>]

print('###############################  Performance Comparison  ##########################################')
arr1 = []
s = time.time()
for i in range(int(1e+6)):
    arr1.append(i)
print('took {} secs'.format(round(time.time() - s, 3)))

s = time.time()
arr2 = [i for i in range(int(1e+6))]
print('took {} secs'.format(round(time.time() - s, 3)))
