class human():
    def __init__(self, age, weight):  # 建立預設屬性的寫法
        self.eye = 2       # 兩個眼睛
        self.ear = 2       # 兩個耳朵
        self.nose = 1      # 一個鼻子
        self.mouth = 1     # 一張嘴巴
        self.age = age             # 讀取參數，變成屬性
        self.weight = weight       # 讀取參數，變成屬性
        self.__password = '預設密碼 0000'

    def say(self, msg):      # 定義 say
        print(f'{self.name} say: {msg}')   # 使用 self.name 取得 name 屬性的值

    def play(self, thing):   # 定義 play
        print(thing)
        
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        self.__password = value


# 從外部定義 hand 和 leg
human.hand = 2    # 定義 hand 屬性
human.leg = 2     # 定義 leg 屬性

kate = human(25, 45)            # 製作一個名為 kate 的物件
print(kate.eye)                 # 得到 2 ( 印出 kate 的 eye 屬性 )。
kate.name = 'kate'              # 設定 name 屬性
kate.say('hello')               # hello
kate.play('baseball')           # baseball
print(kate.hand)                # 2
print(kate.leg)                 # 2
print(kate.age, kate.weight)    # 18, 68

# 覆寫 play 屬性, 覆寫後，去call play 這個 function，會拿到 error( TypeError: 'str' object is not callable).
kate.play = 'volleyball'
print(kate.play)   # volleyball

print(kate.password)
# kate.password = "new pwd"       # If there is no setter, you will get AttributeError: property 'password' of 'human' object has no setter
kate.password = 'new pwd'
print(kate.password)
