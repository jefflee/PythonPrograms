import time
import sys

print("======================  Print  =========================")
print(1, 2, 3)           # 1 2 3
print(1, 2, 3, sep=';')   # 1;2;3
print(1, 2, 3, sep=';', end='!')
print(1, 2, 3)           # 1;2;3!1 2 3

print("======================  Loading  =========================")
print('Loading', end='')
for i in range(6):
    print('.', end='', flush=True)
    time.sleep(0.5)

print("\n======================  Loading 2 | go to the first char position  =========================")
n = 7
for i in range(n+1):
    print(f'\rCountdown {n-i:2} seconds', end='')
    time.sleep(1)
print('\rTime is up', end='')

print("======================  Input from console  =========================")
name = input('Hello, what is your name?  ')
print('Hi,', name)


a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
print(f'Sum={a+b}')