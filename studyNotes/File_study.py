"""
文件操作
1、打开文件
2、读、写文件
3、关闭文件


open: 第一个参数：打开文件名
        存在：返回文件操作对象
        不存在：抛出异常、
      第二个参数：打开方式
        r ： 只读
        w ： 只写，文件不存在就创建，存在就会覆盖
        a :  追加方式打开，若文件存在文件指针就会指向文件末尾，若不存在则创建，并进行写入
        r+ :  以读写的方式打开，如果文件存在文件指向文件开头，不存在就抛出异常
        w+ :  以读写方式打开，如果文件存在就会覆盖，不存在就创建
        a+ :  以读写方式打开文件，若果存在，指向文件结尾，若不存在，就创建文件进行写入


read：一次性读入所有 并 返回所有文件内容
write
close 关闭文件，若未关闭文件造成系统资源消耗，而且影响后续对文件的访问


readline：一次只读取一行内容(防止文件太大，内存消耗大)
方法执行后，文件指针指向下一行，准备再次读取
"""

# 文件基本读写关闭
#  不加入encoding='UTF-8' 会报错 UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 8:
# illegal multibyte sequence
if False:
    file = open("README.txt", encoding='UTF-8')
    txt = file.read()
    print(txt)
    file.close()


"""
文件指针，
文件指针标记从那个位置开始读取数据

第一次打开文件时，通常文件指针会只指向文件开始的位置
执行read后，指向文件末尾
"""
#  readline test
if False:
    file = open("README.txt", encoding='UTF-8')
    while True:
        txt = file.readline()
        if not txt:
            break
        else:
            print(txt)


#  copy 复制小文件
if False:
    file = open("README.txt", encoding='UTF-8')
    file2 = open("README2.txt", "w", encoding='UTF-8')
    txt = file.read()
    file2.write(txt)
    file.close()
    file2.close()


"""
文件、目录的常用管理操作

os模块

文件操作
rename(原文件名， 目标名)
remove(文件名)

目录操作
listdir 目录列表
mkdir   创建目录
rmdir   删除目录
getcwd  获取当前目录
chdir   修改工作目录
path.isdir  判断是否为文件夹

文件和目录操作都支持绝对路径和相对路径
../ 表示的是上层目录
"""

import os

# 上层目录，和目录列表的获取测试
if True:
    # os.renames("README2.txt", "README副本.txt")
    # list2 = os.listdir("C:\\Users\\lammy\\PycharmProjects\\Test\\studyNotes")
    list2 = os.listdir("../studyNotes")
    print(list2)


"""
文本文件的编码格式：
python2x: 默认使用ASCII编码
python3x：默认使用UTF-8编码

ASCII 编码：
计算机只有256个ASCII编码
一个ASCII编码在内存中占用一个字节空间，2的8次方=256 种组合

UTF-8 编码格式
计算机中使用1-6个字节来表示一个UTF-8 字符，涵盖世界上所有地区文字
大多数汉字会使用3个字节表示
UTF-8 是UNI CODE编码的一种编码格式


python2X中使用中文
python2x: 默认使用ASCII编码，若使中文就报错
在python2X文件中的第一行加入代码下面代码 ,就会以utf-8 编码来处理python文件
# *-* coding：utf-8 *-*
上面是官方推荐，也可以使用：
# coding=utf-8

unicode 字符串
在python2.x 中，即使制定了文件使用utf-8 ，但在遍历字符串时，仍然会以字节为单位遍历字符串
如：s = "hello世界"
当一个个字符打时，中文还是乱码
为了打出正确的字符，引号前面加“u”，告诉解释器这是utf-8编码格式字符串
如 s = u"hello世界"
"""