# Refer to https://steam.oxxostudio.tw/category/python/basic/generator.html

print("======================  Comprehension and generator  =========================")
# 產生器是一個 Python 序列製作物件，可以用它來迭代一個可能很大的序列，在迭代的過程中所產生的值都是動態的，不需要將整個序列儲存在記憶體中。
a = [i for i in range(10)]  # 串列生成式
b = (i for i in range(10))  # 產生器表示式
print(a, type(a))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] <class 'list'>
# <generator object <genexpr> at 0x7fbb6facba50> <class 'generator'>
print(b, type(b))

print("======================  Use yield to create a generator  =========================")


def f(max):
    n = 0
    a = 2
    while n < max:
        yield (a)     # 換成 yield
        a = a ** 2
        n = n + 1


g = f(5)
print(type(g))
for i in g:
    print(i, end=', ')
