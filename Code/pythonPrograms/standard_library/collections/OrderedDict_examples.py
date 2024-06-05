from collections import OrderedDict
# 通常建立一個 dict 物件時無法決定 key 的順序，如果使用 OrderedDict 可以創建一個能記錄 key 順序 ( 先進先出 ) 的 dict 物件。

a = OrderedDict()
a['x'] = 2
a['y'] = 3
a['z'] = 1
for x in a:
    print(x)
    
print(a)   # rderedDict([('x', 2), ('y', 3), ('z', 1)])
