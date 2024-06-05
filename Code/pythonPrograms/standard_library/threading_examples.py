import time
from concurrent.futures import ThreadPoolExecutor

print("======================  concurrent.futures ThreadPoolExecutor   =========================")


def test(n):
    for i in range(n):
        print(i, end=' ')
        time.sleep(0.2)
    print('\nA thread completed.\n')


with ThreadPoolExecutor() as executor:
    executor.map(test, [2, 3, 4])
