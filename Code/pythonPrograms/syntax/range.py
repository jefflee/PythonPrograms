# Range
r1 = range(10)
r2 = range(5, 50, 5)

print(type(r1))  # <class 'range'>
print(r1)  # range(0, 10)
print(r2)  # range(5, 50, 5)

for i in r1:
    print(f"{i} ", end='')

print('\n***')

for i in r2:
    print(f"{i} ", end='')
