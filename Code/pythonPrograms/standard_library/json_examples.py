import json

# Refer to
# https://steam.oxxostudio.tw/category/python/library/json.html

print("======================  load(fp)   =========================")
# json.load() 的參數是給一個file
jsonFile = open('file_test_folder/test_pet.json', 'r')
a = json.load(jsonFile)
for i in a:
    print(i, a[i])


print("======================  loads(s)   =========================")
# json.loads() 的參數給的是一個 string
jsonFile = open('file_test_folder/test_pet.json', 'r')
f = jsonFile.read()   # 要先使用 read 讀取檔案
a = json.loads(f)      # 再使用 loads
for i in a:
    print(i, a[i])

print("======================  dumps(obj)   =========================")
data = {}
data['name'] = 'oxxo'
data['age'] = 18
data['eat'] = ['apple','orange']
json_string = json.dumps(data, indent=2,)     # 產生要寫入的資料

print(json_string)
