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

    # list to tuple 数据能修改变为不可修改，保护数据
    num_tuple = tuple(num_list)
    print(type(num_tuple))

    # tuple to list 数据从不能修改表为能
    num_list2 = list(num_tuple)
    print(type(num_list2))


list_tuple_convert(False)
