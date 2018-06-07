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


"""
列表（其他语言中称为数组） 
1、存储相同类型的数据
2、也是支持不同类型数据存储的，用的极少
遍历效率高，一般用迭代器，for来遍历
"""


def list_test(test):
    """
    :param test:
    :return:
    """
    if not test:
        return
    # 列表的赋值
    names = ["zs", "ls", "ww"]
    print(names[1])

    # 增加
    # 增加 insert
    names.insert(0, "zl")
    print("insert: ")
    print(names)
    # 增加 append ， 是在列表末尾添加元素，若是其他数据结构也是直接添加，若是a = [1,2],b = [3, 4]  则a.append(b) = [1, 2, [3, 4]]
    names.append("Ll")
    print("append: ")
    print(names)
    # 列表拼接
    names2 = ["aa", "bb"]
    names.extend(names2)
    print("extend: ")
    print(names)

    # 修改
    names[0] = "cc"
    print("第0个修改为cc修改: ")
    print(names)

    # del删除
    print("del 删除第一个元素")
    del names[0]
    print(names)
    # 删除 __delitem__
    names.__delitem__(0)
    print("删掉第0个数据: ")
    print(names)
    # remove 删除 第一个出现的数据
    names.remove("Ll")
    print("删掉zs数据: ")
    print(names)
    # pop 删除最后一个数据
    print("删掉 pop 末尾数据: ")
    names.pop()
    print(names)
    # pop 删除pop第二个参数
    names.pop(2)
    print("删掉 pop 第二个数据: ")
    print(names)
    # clear删除全部，清空列表
    names.clear()
    print("清空列表")
    print(names)

    # 统计
    # 长度 len
    length = names.__len__()
    print("names 长度")
    print(length)
    names = ["aa", "aa", "bb", "cc", "aa"]
    # count 出现某个元素的次数
    count = names.count("aa")
    print("names 出现aa的次数")
    print(names)
    print(count)

    # 排序
    # sort 默认升序排列
    print("升序排列")
    names.sort()
    print(names)
    print("降序排列")
    names.sort(reverse=True)
    print(names)
    # 反转
    print("反转")
    names.reverse()
    print(names)

    # 遍历
    for name in names:
        print(name)


list_test(False)


"""
元组(tuple)：和数组很类似，区别在于：
1、元组的数据不能修改（类似于java枚举）
2、定义的时候用() 而列表用[]
例子：
info_tuple = ("ZhangSan", 18, 1.75)

使用场景：
1、 函数的 参数 或 返回值，可任意传入和返回多个数据
2、格式化字符串
3、让列表不可以修改，类似枚举
"""


def tuple_test(test):
    if not test:
        return
    info_tuple = ("ZhangSan", 18, 1.75)
    print(type(info_tuple))
    print(info_tuple[2])
    # 空元组
    empty_tuple = ()
    print(type(empty_tuple))
    # 单元组
    single_tuple = (5,)  # 定义成（5） 则解释器认为整型了

    # index 18第一次出现的索引
    index = info_tuple.index(18)
    # 统计出现的次数
    number = info_tuple.count(1.75)
    print("18出现的索引值为: %d" % index)
    print(number)
    # 遍历
    for tuple_member in info_tuple:
        print(tuple_member)

    # 格式化字符串,后面的"( )" 本质上就是元组
    print("%s 年龄是 %d 身高是 %.2f" % ("ZhangSan", 18, 1.75))
    print("%s 年龄是 %d 身高是 %.2f" % info_tuple)


tuple_test(False)


def list_tuple_convert(test):
    if not test:
        return
    num_list = [1, 2, 3, 4]

    # list to tuple 数据能修改变为不可，保护数据
    num_tuple = tuple(num_list)
    print(type(num_tuple))

    # tuple to list 数据从不能修改表为能
    num_list2 = list(num_tuple)
    print(type(num_list2))


list_tuple_convert(False)


"""
字典（dictionary）: 通常用来存储描述一个物体的相关信息
和列表的区别:
1、列表是有序的对象集合
2、字典是无序的对象集合
3、字典用{}定义

字典用 键值对 存储数据，键值对之间用 ，隔开
键 key 是索引
值 value 是数据
键 值 之间用 : 隔开
键必须是唯一的
值可以是任何数据类型，但键只能是字符串、数字、元组
"""


def dictionary_test(test):
    if not test:
        return
    xiaoming = {
        "name": "xiaoming",
        "age": 18,
        "gender": True,
        "height": 1.75
    }
    print(xiaoming)

    # 取值 , [] 内是key, 若不存在就会报错
    name = xiaoming["name"]
    print("姓名 name = %s" % (name,))

    # 增加
    xiaoming["telephone"] = "13232880562"
    print("增加电话号码")
    print(xiaoming)

    # 修改
    xiaoming["telephone"] = "18680354007"
    print("修改电话号码")
    print(xiaoming)

    # 删除 key不存在会报错
    xiaoming.pop("telephone")
    print("删除电话号码信息")
    print(xiaoming)

    # len统计键值对的数量
    length = xiaoming.__len__()
    print("length = %d" % length)

    # update 合并临时字典,若原来就有键值对则会覆盖原来的键值对
    temp_dict = {"telephone": 18680354007}
    xiaoming.update(temp_dict)
    print("合并电话号码信息的字典")
    print(xiaoming)

    # 清空键值对
    xiaoming.clear()
    print("清空字典")
    print(xiaoming)

    # 遍历
    xiaoming = {
        "name": "xiaoming",
        "age": 18,
        "gender": True,
        "height": 1.75
    }
    print("遍历：")
    for k in xiaoming:
        print("%s : %s" % (k, xiaoming[k]))


dictionary_test(True)


"""
字符串 str
python 可以用一对 双引号 或者 单引号来定义字符串，一般用双引号，当字符串中用到双引号的时候，可以用单引号
例：
str = '我的外号是"大西瓜"'

可以通过索引取字符值
"""


def str_test(test):
    if not test:
        return
    # 遍历
    two_name = '我的外号是"大西瓜"'
    for s in two_name:
        print(s)

    test_str = "hello hello !"
    # len 长度
    length = test_str.__len__()
    print("长度是：%d" % length)

    # count 统计子字符串出现的次数
    count_num = test_str.count("hello")
    print("hello 出现的次数%d" % count_num)

    # index 出现子字符串出现的位置，若子字符串不存在，会报错
    index = test_str.index("llo")
    print("llo 出现的位置： %d" % index)


str_test(True)

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