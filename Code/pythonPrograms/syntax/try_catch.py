
print("======================  try catch  =========================")
try:
    print(1/0)
except TypeError:
    print('型別發生錯誤')
except NameError:
    print('使用沒有被定義的對象')
except Exception as e:
    print('不知道怎麼了，反正發生錯誤惹')
    print(e)
print('hello')

print("======================  Raise error  =========================")
try:
    # a = int(input('輸入 0～9：'))
    a = 11
    if a > 10:
        raise ValueError('數字不在範圍內')
    print(a)
except ValueError as msg:    # 如果輸入範圍外的數字或解析非 10 進位數字，執行這邊的程式
    print(msg)
except:                     # 其他錯誤，執行這邊的程式
    print('有錯誤喔～')
print('繼續執行')

print("======================  assert  =========================")
# assert 語句用於檢查條件是否為真。如果條件為假，則觸發 AssertionError 異常。
# 通常用於檢查開發者預期為真的條件，以確保代碼的正確性。
try:
    a = 11
    if a > 10:
        assert False, '數字不在範圍內'
    print(a)
except AssertionError as msg:
    print(msg)
except:
    print('有錯誤喔～')
print('繼續執行')

print("======================  else and final  =========================")
try:
    a = 11
    if a > 10:
        raise
    print(a)
except:
    print('有錯誤喔～')
else:
    print('沒有錯！繼續執行！')       # 完全沒錯才會執行這行
finally:
    print('管他有沒有錯，繼續啦！')    # 不論有沒有錯都會執行這行
