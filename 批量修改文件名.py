# Feb, 27th, 2018 @ dormitory 5# R627
# 批量修改文件名
import os
path = 'E:/Don\'t let language limit your world/TomatoEnglish/test'
count = 0
# os.listdir(path) 返回一个文件名列表
for file_name in os.listdir(path):
    # 切片获取文件扩展名
    if file_name[-3::] == 'txt':
        count += 1
        # 新文件名控制
        new_name = str(count) + '.txt'
        # os.rename 的参数要写全文件路径
        os.rename(path + '/' + file_name,path + '/' + new_name)
