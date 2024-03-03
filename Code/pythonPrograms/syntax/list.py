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

print('###############################  List Update Operation  ##########################################')
print('###########  s[i:j]  ###########')
# s[i:j] = t | index從i到j的元素內容置換為X
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst[1:2] = [0, 0]
print(f"lst[1:2] = [0, 0] \t\t-> {lst}")

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst[1:2] = [0, 0, 0]
print(f"lst[1:2] = [0, 0, 0] \t-> {lst}")

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst[1:3] = [0, 0]
print(f"lst[1:3] = [0, 0] \t\t-> {lst}")

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst[1:3] = [0, 0, 0]
print(f"lst[1:3] = [0, 0, 0] \t-> {lst}")

print('######################')
# s[i:j:k] = t | index從i到j的元素，以step為k的方式，將內容置換為X
# todo: need to find out an example
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lst[0::2] = [0,0]
# print(f"lst[0::2] = [0] \t-> {lst}")

# del s[i:j] | 把index從i到j的元素刪除
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lst[1:3]
print(f"del lst[1:3] -> {lst}")  # [1, 4, 5, 6, 7, 8, 9, 10] index 3 也被刪了

# del s[i:j:k] | index從i到j的元素，以step為k的方式刪除元素
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lst[1::2]
print(f"del lst[1::2] -> {lst}")  # [1, 3, 5, 7, 9]

# s.append(x) | 將X塞到S容器的最後面
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst.append(11)
print(f"lst.append(11) -> {lst}")  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# s.clear() | 將S容器的內容全部刪除(same as del s[:])
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst.clear()
print(f"lst.clear() -> {lst}")  # []

# s.copy() | 複製S容器(same as s[:])
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = lst.copy()
print(f"lst2 = lst.copy() -> {lst2}")  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"lst2 is lst -> {lst2 is lst}")  # False

# s.extend(t) | 同 s = s + t
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst.extend([11, 12, 13])
print(f"lst.extend([11, 12, 13]) -> {lst}")  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# s.insert(i,x) | 在S容器index為i的位置將X插入，原有的元素(們)將會往後移
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst.insert(1,'a')
print(f"lst.insert(1,'a') -> {lst}")  # [1, 'a', 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst.insert(1,['a','b'])
print(f"lst.insert(1,['a','b']) -> {lst}")  # [1, ['a', 'b'], 2, 3, 4, 5, 6, 7, 8, 9, 10]

# s.pop(i) | 將index為i的元素取出，並將其移出容器
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
val = lst.pop(2)
print(f"val = lst.pop(2) -> val={val}, lst={lst}")  # val=3, lst=[1, 2, 4, 5, 6, 7, 8, 9, 10]

# s.remove(x) | 刪除第一個找到的X
lst = [1, 2, 3, 4, 5, 2]
lst.remove(2)
print(f"lst.remove(2) -> {lst}")  # [1, 3, 4, 5, 2]

# s.reverse() | 讓容器的內容順序顛倒
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst.reverse()
print(f"lst.reverse() -> {lst}")  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
