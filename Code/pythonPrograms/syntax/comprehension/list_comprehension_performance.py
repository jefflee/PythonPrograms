from timeit import timeit


def with_for():
    lst = []
    for i in range(100):
        lst.append(i)
    return lst


def without_for():
    return [i for i in range(100)]


def list_convertor():
    return list(range(100))


print(f'with:           {timeit(with_for, number=10000)}')
print(f'without_for:    {timeit(without_for, number=10000)}')
print(f'list_convertor: {timeit(list_convertor, number=10000)}')
