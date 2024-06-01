"""
string built-in functions.
https://steam.oxxostudio.tw/category/python/basic/string-all.html#a00
https://steam.oxxostudio.tw/category/python/basic/string-all.html#a01

Rstring format
https://steam.oxxostudio.tw/category/python/basic/format.html#a2

f-string
https://steam.oxxostudio.tw/category/python/basic/format.html#a3

string operation and conversion
https://steam.oxxostudio.tw/category/python/basic/builtin-string.html

"""

# string
str1 = 'hello python'
str2 = str1
str2 += ' journey'
print(str2 is str1)  # False -> string is immutable

print(str1)  # hello python -> string is immutable

print(len(str1))  # 12

# split by space
result = str2.split(' ')
print(result) # ['hello', 'python', 'journey']

# join by ***
result_back = '***'.join(result)
print(result_back)  # hello***python***journey

print('=======================  slice  ==============================')
# The string first char
str3 = 'abcd'
print(str3[0])  # can print the first char, but cant set it.

a = '0123456789abcdef'
print(a[:])       # 0123456789abcdef ( 取出全部字元 )
print(a[5:])      # 56789abcdef ( 從 5 開始到結束 )
print(a[:5])      # 01234 ( 從 0 開始到第 4 個 ( 5-1 ) )
print(a[5:10])    # 56789 ( 從 5 開始到第 9 個 ( 10-1 ) )
print(a[5:-3])    # 56789abc ( 從 5 開始到倒數第 4 個 ( -3-1 ) )
print(a[5:10:2])  # 579 ( 從 5 開始到第 9 個，中間略過 2 個 )

print('=======================  print ok  ==============================')
# print ok 10 times
str_ok = 'ok'*10
print(str_ok) # okokokokokokokokokok

# print ok 20 times
a = 'ok'*5
b = a * 4
print(b)


print('=======================  find  ==============================')
a = 'hello world, I am oxxo, I am a designer!'
b = a.find('am')
c = a.rfind('am')
print(b)  # 15 ( 第一個 am 在 15 的位置 )
print(c)  # 26 ( 最後一個 am 在 26 的位置 )

print('=======================  startwith, endwith, isalnum, count  ==============================')
a = 'hello world, I am oxxo, I am a designer!'
b = a.startswith('hello')
c = a.endswith('hello')
d = a.isalnum()
e = a.count('am')
print(b)   # True  ( 開頭是 hello )
print(c)   # False ( 結尾不是 hello )
print(d)   # False ( 裡面有逗號和驚嘆號 )
print(e)   # 2 ( 出現兩次 am )

print('=======================  title, upper, lower, swapcase  ==============================')
a = 'Hello world, I am OXXO'
b = a.title()
c = a.upper()
d = a.lower()
e = a.swapcase()
print(b) # Hello World, I Am Oxxo
print(c) # HELLO WORLD, I AM OXXO
print(d) # hello world, i am oxxo
print(e) # hELLO WORLD, i AM oxxo

print('=======================  f-string add 0 to left until length is 3  ==============================')
for i in range(1,101):
  print(f'{i:03d}',end=' , ')