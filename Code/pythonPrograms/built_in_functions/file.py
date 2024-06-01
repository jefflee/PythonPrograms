# Refer to
# https://steam.oxxostudio.tw/category/python/basic/builtin-open.html

print("======================  open()  =========================")
f = open('file_test_folder/test_read.txt', 'r', encoding="utf-8")
a = f.read()
print(a)
f.close()

print("======================  use with  =========================")
# 使用 with 可以讓開啟檔案，執行相關內容後自動關閉並釋出記憶體

with open('file_test_folder/test_read.txt', 'r', encoding='utf-8') as f1:
    a = f1.read()
    print(a)
    # 完成後如果沒有後續動作，就會自動關閉檔案

print("======================  Write file and override every time  =========================")
with open('file_test_folder/test_write.txt', 'w', encoding='utf-8') as f1:
    f1.write('good morning')

print('Write completed')
