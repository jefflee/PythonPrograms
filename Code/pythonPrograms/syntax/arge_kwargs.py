print("======================  *args  =========================")
def test(*args):
    print(args)
    print(type(args))       # <class 'tuple'>

# 如果把函式的參數設定帶有 args ( 一個星號 * ) 運算子的參數，則傳入的所有參數，都會被組合成 tuple 的型態，
test(1,2,3,'a','b','c')

print("======================  *kwargs  =========================")
def test2(**kwargs):
    print(kwargs)
    print(type(kwargs))     # <class 'dict'>

# 如果把函式的參數設定帶有 kwargs ( 兩個星號 ** ) 運算子的參數，則傳入的所有「帶有關鍵字引數」的參數，都會被組合成字典的型態
test2(name='oxxo',age=18,like='book')

print("======================  Put * in front of the parameter in invocation  =========================")
# 如果將一個星號套用在 print() 裡 ( print() 算是一個內建函式 )，就會將可迭代的物件打散後印出。
a = [1,2,3,4,5]
b = (1,2,3,4,5)
c = {'x':1,'y':2,'z':3}
d = {'x','y','z'}

print(*a)   # 1 2 3 4 5
print(*b)   # 1 2 3 4 5
print(*c)   # x y z
print(*d)   # x y z
print(*{'x':1,'y':2,'z':3})
