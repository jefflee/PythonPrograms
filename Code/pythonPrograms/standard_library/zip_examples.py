import os
import zipfile

# 刪除已經存在的檔案
target_folder = 'file_test_folder/zip/'
target_file = 'zipedFile.zip'

if os.path.exists(target_folder + target_file):
    os.remove(target_folder + target_file)


print("======================  zip files  =========================")
with zipfile.ZipFile(target_folder+target_file, mode='w') as zf:
    zf.write(target_folder+'1.png')
    zf.write(target_folder+'2.png')
print('zip successfully.')

print("======================  unzip a zip file  =========================")
# zf.extract(name, path, pwd)
# name 要解壓縮的檔案名稱
# path 解壓縮後要放的位置
# pwd 解壓縮密碼
# 若目地的已經有檔案的話，則不會覆蓋。
with zipfile.ZipFile(target_folder + 'test.zip', mode='r') as zf:
    nameList = zf.namelist()
    for name in nameList:
        zf.extract(name, 'file_test_folder/zip/unzip_folder')
print('unzip sucessfully')
