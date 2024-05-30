# variables and types
iv = 10
fv = 12.3
cv = 3 + 5j
sv = 'hello python'
bv = True
nv = None

print(iv, fv, cv, sv, bv)
print(type(iv))  # <class 'int'>
print(type(fv))  # <class 'float'>
print(type(cv))  # <class 'complex'>
print(type(sv))  # <class 'str'>
print(type(bv))  # <class 'bool'>
print(nv)  # None
print(isinstance(sv, str))  # True

print('=============================================')

a = (1,)
b = ('b',)
c1 = a
c2, = a    # add ',' after variable name
d1 = b
d2, = b    # add ',' after variable name
print(c1, type(c1))  # (1,) <class 'tuple'>    # still tuple
print(c2, type(c2))  # 1 <class 'int'>         # become int
print(d1, type(d1))  # ('b',) <class 'tuple'>  # still tuple
print(d2, type(d2))  # b <class 'str'>         # become string

print('===================  Convert to int  ==========================')
print(int(5.1))     # 5
print(int(9/2))     # 4
print(int('5'))     # 5
print(int('+2'))    # 2
print(int(True))    # 1
print(int(False))   # 0

print(int('101', 2))    # 5   binary
print(int('101', 8))    # 65  octal
print(int('101', 16))   # 257 hexadecimal

print('===================  binary, octal, hexadecimal  ==========================')
print(0b1111)  # 15 ( binary )
print(0B1111)  # 15 ( binary )
print(0o1111)  # 585 ( octal )
print(0O1111)  # 585 ( octal )
print(0x1111)  # 4369 ( hexadecimal )
print(0X1111)  # 4369 ( hexadecimal )

print('===================  Convert to bool ==========================')
print(bool(True))   # True
print(bool(1))      # True
print(bool('ok'))   # True
print(bool(-1))     # True
print(bool(-1))     # True
print(bool(2))      # True
print(bool(2.0))      # True

print(bool(False))  # False
print(bool(0))      # False
print(bool(0.0))    # False

