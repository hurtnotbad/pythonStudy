"""
while 循环：根据缩进为一个代码块
基本语法
while 条件（判断、计数器、是否到达目标次数）：
    条件满足执行的语句
    ...
    处理条件（计数器+1）
"""


def while_test(test):
    if not test:
        return
    i = 0
    while i < 10:
        print("i love you !")
        i = i + 1
        if i == 7:
            print("说了 7 遍了")
            continue
        if i == 9:
            print("说了9遍可，最后一遍不说了")
            break


while_test(False)


