print("======================  decorator without parameters  =========================")
def a(func):
    print('makeup...')
    return func

# 裝飾器寫在 b 的前面，表示裝飾 b
@a
def b():
    print('go!!!!')

b()
# makeup...
# go!!!!

print("======================  decorator with a parameter  =========================")
def a(func):
    def c(m):             # 新增一個內部函式，待有一個參數
        print('makeup...')
        return func(m)      # 回傳 func(m)
    return c

@a
def b(msg):
    print(msg)

b('go!!!!')
# makeup...
# go!!!!

print("======================  multiple decorators  =========================")
# 執行的順序將會「由下而上」觸發 ( 函式一層層往上 )，下方的程式碼，會先裝飾 a3，接著裝飾 a2，最後裝飾 a1。
def a1(func):
    print('1')
    return func

def a2(func):
    print('2')
    return func

def a3(func):
    print('3')
    return func

@a1
@a2
@a3
def b():
    print('go!!!!')

b()
# 3
# 2
# 1
# go!!!!
