print('\n*** Zip 2 list ***')
arr1 = [i for i in range(1, 21, 2)]
arr2 = [i for i in range(2, 21, 2)]

# Sol1: use 2 variables to handle value
for o, e in zip(arr1, arr2):
    print(o, e, sep=' <---> ')

# Sol2: use tuple to handle value
for t in zip(arr1, arr2):
    print(t[0], t[1], sep=' <---> ')
