class father():
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1


class mother():          # mother 類別
    def __init__(self):
        self.nose = 2
        self.hair_color = 'blonde'

    def language(self):  # mother 的方法
        print('english')

    def skill(self):
        print('painting')


class son(father, mother):
    def __init__(self):
        # 多重繼承為了將所有 parents 的 __init__ 都呼叫過，只好這樣寫。單一繼承時，可以看下面用 super() 就好了。
        father.__init__(self)
        mother.__init__(self)
        
        # super().__init__()   # 使用 super() 繼承 father __init__ 裡所有屬性
        
        self.eye = 100       # 如果屬性相同，則覆寫屬性

    def play(self):           # son 自己的方法
        print('ball')


kate = son()
print(kate.eye)              # 100
print(kate.ear)              # 2
print(kate.nose)             # from mother
kate.skill()                 # from mother
kate.play()                  # himself
print(kate.hair_color)       # from mother
