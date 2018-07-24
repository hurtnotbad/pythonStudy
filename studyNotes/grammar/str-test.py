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