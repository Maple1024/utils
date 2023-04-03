import os
import shutil


image_name="image"
lable_name="lable"
if not  os.path.exists(image_name):
    os.makedirs(image_name)
if not os.path.exists(lable_name):
    os.makedirs(lable_name)

current_path=os.getcwd()
print('当前目录: ',current_path)
filename_list=os.listdir(current_path)

for k in filename_list:
    if k.endswith(".jpg"):
        shutil.move(k,image_name)
    if k.endswith(".txt"):
        shutil.move(k,lable_name)
files=os.listdir(image_name)
print("dataszise= ",len(files))
files=os.listdir(lable_name)
print("lablesize= ",len(files))
