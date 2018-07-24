"""
python数据类型是根据左端存储的数据推断变量的数据类型的
数据类型

数字型：
bool true:非0数，false：0 非零即真;参与数字运算时，false = 0 true = 1
int
long(python 2.x中含有，在python3中去掉了，不需要区分是int还是long，所有的整型都归为int型)
float

非数字型：
字符串(str)  用""
列表
元组
字典

"""

"""
不可变类型：当作在函数中修改参数，不会影响原来传入的变量值
数字类型：int bool ,float,complex ，long（python 2.x）
字符串 str
元组 tuple

可变类型：当作在函数中修改参数，会修改原来传入的变量值
列表 list
字典 dict
"""

"""
python 内置函数（针对高级数据类型的操作：列表、元组、字典、字符串）
len(item) : 计算容器的长度
del(item) 删除变量，如列表中的元素
max(item)  返回容器中元素最大值，若是字典时候，针对key来比较
min(item) 返回容器中最小值  若是字典时候，针对key来比较
cmp(item1, item2)  比较2个值-1 小于； 0 相等 ； 1 大于 python3 取消了此函数（可以用字符比较 列表、元组进行比较，无法对字典进行比较）
[2, 2, 2] > [1, 1, 1]
(2， 2， 2)> （1， 1， 1）
"""

"""
python 切片
字符串、列表、元组支持切片，字典不行
例：
a = [1, 2, 3, 4][1:3]  得到的结果为 a = [2, 3]
"""

"""
运算符          python表达式               结果                                 描述           支持数据类型
  +           [1, 2] + [3, 4]           [1, 2, 3, 4]                           合并           str、tuple、list
  *            ["Hi!"]*4                ["Hi!", "Hi!", "Hi!", "Hi!", ]         重复           str、tuple、list
  in           3 in (1, 2, 3)              True                               元素是否存在     str、tuple、list、dictionary
  not in
> >= == < >=    (1, 2, 3)< (2, 2, 3)       True                                元素比较        str、tuple、list


"""

# 不同类型的运算


def test_bool_int(test):
    """
    数字类型的变量可以直接参与运算，bool 中false = 0 true = 1
    :param test:
    :return:
    """
    if not test:
        return
    a = False
    b = True
    print(a + 0)
    print(b + 0)


test_bool_int(False);


def test_bool_int(test):
    """
    字符串操作 , 字符串之间可直接拼接; 字符串不能与数字型相加，但可以相乘
    :param test:
    :return:
    """
    if not test:
        return
    a = "张"
    b = "三"
    c = a + b
    print(c)
    d = (a + b) * 10
    print(d)


test_bool_int(False)


def int_float_convert(test):
    """
    int float 数据转化
    :param test:
    :return:
    """
    if not test:
        return
    a = "3.2"
    b = float(a)
    c = int("32")
    print(type(b))
    print(type(c))


int_float_convert(False)
