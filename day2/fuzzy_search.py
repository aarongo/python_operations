#_*_coding:utf-8_*_
#创建空list
list = []
#记录出现的次数
appear_count = 0
#循环状态
status = True
#读取文件
information = file("E:\pythonworks\works\day2\info.txt")
#读取文件全部行数readlines，添加到list中
for line in information.readlines():
#去掉文件中的换行符
    list.append(line.replace("\n",""),)
information.close()
''' #1 循环字符串str 在List中
    #2 判断输入的模糊查询时候存在list中
    #3 输出包含模糊查询的字符串在list中
    #4 每查到一个 计数+1
    #5更改外层循环状态
    #6判断外层循环状态，确定是否重新查找
    #7 输出查询的总结果
'''
while status:
    #输入模糊查询的字符串-->一个集合
    str_input = raw_input("Please Your Find String:")
    #定义需要高亮的字符串
    new_string = "\033[40;32m%s\033[0m" % str_input
    for str in list:#1
        if str.startswith(str_input):#2
            print str.replace(str_input,new_string),#3
            appear_count += 1#4
            status = False #5
    if status == True: #6
        print "\033[40;32m 请重新查找 \033[0m"
print "\nThe character appeared：\033[40;32m %s \033[0m" %(appear_count)#7