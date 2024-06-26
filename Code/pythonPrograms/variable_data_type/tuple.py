# Tuple - Can put parentheses as well.
t1 = 10, 20
# it can hold different types of data
t2 = 10, 'hello world'

print(type(t1)) # <class 'tuple'>
print(t1)       # (10, 20)
print(t2)       # (10, 'hello world')
print(len(t2))  # 2

print("====================  Split tuple into multiple variables.  =======================")
t = ('apple','banana','orange','grap')
a, b, c, d = t
print(a)   # apple
print(b)   # banana
print(c)   # orange
print(d)   # grap