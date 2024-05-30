print("======================  Declaration  =========================")
a = {'name':'oxxo','age':18,'eat':['apple','banana']}
print(type(a));    # <class 'dict'>

# An empty dictionay
a = {}
print(type(a)); 

print("======================  Convert tuple to dictionary  =========================")
a = [['x','100'],['y','200'],['z','300']]
b = dict(a)
print(b)    # {'x': '100', 'y': '200', 'z': '300'}

a = ['ab','cd','ef']
b = dict(a)
print(b)    # {'a': 'b', 'c': 'd', 'e': 'f'}

print("======================  setdefault()  =========================")
a = {'name':'oxxo', 'age':18}
b = a.setdefault('age', 100)
c = a.setdefault('ok', True)
print(a)   # {'name': 'oxxo', 'age': 18, 'ok': True}
print(b)   # 18
print(c)   # True

print("======================  del  =========================")
# delete the key 'name'
a = {'name':'oxxo', 'age':18}
del a['name']
print(a)   # {'age': 18}

# delete the dictionary
b = {'name':'oxxo', 'age':18}
del b
# print(b)   # name 'b' is not defined

print("======================  pop  =========================")
a = {'name':'oxxo', 'age':18}
b = a.pop('name')
print(a)   # {'age': 18}
print(b)   # oxxo

print("======================  clear  =========================")
a = {'name':'oxxo', 'age':18}
a.clear()
print(a)   # {}
