"""
if基本语法：根据缩进为一个代码块
if 条件1：
    条件成立时，要做的事情
    ....
    （无缩进时候结束if模块）
    if 条件1-1：
        满足条件1 、1-1时候执行的代码
elif 条件2
    不条件满足1，满足条件2 要做的事情
    ....
elif 条件3
    不满足条件1、2，满足条件3
    ....
else:
    所有条件不成立时执行
    ...
Node: 注意缩进为一个tab 或者四个空格（但不要有的地方用tab 有的地方用空格,最好一致 ，官方建议用空格）
"""


def if_test(test):
    if not test:
        return
    age = int(input("请输入年龄"))
    # if age >= 18 and age < 100:  要用简单形式表示，这样就会提出警告：simplify chained comparision
    if 18 <= age < 100:
        print("可以进入网吧")
        print("欢迎光临！")
        if 18 <= age <= 21:
            print(" 请合理安排时间，您还在读书！")
    elif age >= 100:
        print("您年纪太多")
    else:
        print("您还未满18岁")
        print("请您满18岁后来上网")


if_test(False)
"""
循环中断：
break : 退出循环
continue ： 退出当次循环，继续循环 
"""

"""
for 循环语句
迭代器遍历列表效率高
for 变量 in 集合：
    循环体代码
else:
    没有通过break 退出循环，循环结束后会执行
"""


def for_test(test):
    if not test:
        return
    names = ["zs", "ls", "ww", "zl"]
    for name in names:
        print(name)


for_test(True)
