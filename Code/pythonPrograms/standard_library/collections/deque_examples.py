from collections import deque

a = deque(['a','b','c','d','e'])   # 建立 deque 物件

a.append('x')
a.append('y')        # 在最右邊加入元素
print(a)             # deque(['a', 'b', 'c', 'd', 'e', 'x', 'y'])

a.appendleft('x')
a.appendleft('y')    # 在最左邊加入元素
print(a)             # deque(['y', 'x', 'a', 'b', 'c', 'd', 'e', 'x', 'y'])

b = a.copy()         # 淺拷貝
print(b)             # deque(['y', 'x', 'a', 'b', 'c', 'd', 'e', 'x', 'y'])

print(a.count('x'))  # 2，計算 x 出現的次數

a.extend(['m','n'])  # 在最右邊加入 ['m','n']
print(a)             # deque(['y', 'x', 'a', 'b', 'c', 'd', 'e', 'x', 'y', 'm', 'n'])

a.extendleft(['m','n'])  # 在最左邊加入 ['m','n']
print(a)                 # deque(['n', 'm', 'y', 'x', 'a', 'b', 'c', 'd', 'e', 'x', 'y', 'm', 'n'])

print(a[5])      # b，取出第六個元素 ( 第一個為 0 )

a.insert(1,'k')  # 在第二個位置插入 k
print(a)         # deque(['n', 'k', 'm', 'y', 'x', 'a', 'b', 'c', 'd', 'e', 'x', 'y', 'm', 'n'])

a.pop()          # 移除最右邊的元素
print(a)         # deque(['n', 'k', 'm', 'y', 'x', 'a', 'b', 'c', 'd', 'e', 'x', 'y', 'm'])

a.popleft()      # 移除最左邊的元素
print(a)         # deque(['k', 'm', 'y', 'x', 'a', 'b', 'c', 'd', 'e', 'x', 'y', 'm'])

a.remove('x')    # 移除第一個 x
print(a)         # deque(['k', 'm', 'y', 'a', 'b', 'c', 'd', 'e', 'x', 'y', 'm'])

a.reverse()      # 反轉
print(a)         # deque(['m', 'y', 'x', 'e', 'd', 'c', 'b', 'a', 'y', 'm', 'k'])

a.rotate(5)      # 往右邊移動五格
print(a)         # deque(['b', 'a', 'y', 'm', 'k', 'm', 'y', 'x', 'e', 'd', 'c'])

a.clear()        # 清空項目
print(a)         # deque([])