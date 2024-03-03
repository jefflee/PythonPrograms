# List( Array)
# 陣列內的資料型別不必相同
arr1 = [1, 2, 3]
arr2 = [10, 'hello world', 8.7]
arr1[0] = [1, 2, 3]

print(type(arr1))
print(arr1)
print(arr2)

print('###############################  Slice array  ##########################################')

str1 = 'hello world'
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# seq[start:stop:step]
arr2 = arr1[0:5]

# -1 represent the last element
arr3 = arr1[0:-1:2]

# you can ignore the args...
arr4 = arr1[:]

print(len(arr1))  # 10
print(arr2)  # [1, 2, 3, 4, 5]
print(arr3)  # [1, 3, 5, 7, 9]
print(arr4)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr4 is arr1)  # False  -> arr4 and arr1 are not the same memory.
print(str1[5:])  # " world"  -> There is a space in the beginning.
print(arr1[:-1])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('###############################  List Operations  ##########################################')

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# x in s | 檢查X是否存在於S這個容器之中
if 2 in lst:
    print('2 is in lst')

# x not in s | 檢查X是否不存在於S這個容器之中
if 'abc' not in lst:
    print('abc is not in lst')

# s + t | 容器S與容器T的內容相加
s = [1, 2, 3]
t = [4, 5, 6]
print(s + t)  # [1, 2, 3, 4, 5, 6]

# s * n | 三個容器S => s + s + s
print(s * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# len(s) | 取得容器的長度 (裡面有幾個元素的意思)
print(f"len(s): {len(s)}")  # 3
print(f"len(s*3): {len(s * 3)}")  # 9

# min(s) | 取得容器內的最小值 (前提是裡面的元素要能比大小啊!)
print(f"min(lst): {min(lst)}")  # 1

# max(s) | 取得容器內的最大值
print(f"max(lst): {max(lst)}")  # 10

# sum(s) | sum all elements
print(f"sum(lst): {sum(lst)}")  # 55

print(f"type(lst): {type(lst)}")  # <class 'list'>

# s.index(x[,i[,j]]) | X元素在S容器的索引值，如果有給i, j就只會在index為i~j的範圍找
# 找不到會拿到 ValueError 的錯誤
print(f"lst.index(2): {lst.index(2)}")  # 1
print(f"lst.index(2, 0): {lst.index(2, 0)}")  # 1
print(f"lst.index(2, 0, 5): {lst.index(2, 0, 5)}")  # 1

# s.count(x) | X這個元素在S這個容器內出現幾次
print(f"lst.count(2): {lst.index(2)}")  # 1 -> 2 出現 1 次
