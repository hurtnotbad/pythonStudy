"""

*****************************函数的相关基本知识****************************************


函数的定义：函数定义与上一行得空2行，多了少了都会警告，因此注释函数不是在函数的上面注释，而是在定义下面
用下面方式生成注释文档，在调用该函数的地方使用ctr + Q 就可以查看到注释文档

def name(arg1， arg2):
   “”“（格式问题，我这用了中文引号，实际操作用引文引号）
    解释文档
   “””
   ...
   ...

其他python文件若想使用此方法，则需要import 此文件，然后 “文件名.函数名” 的方式来调用

函数的返回值
1、在函数定义中，结束时候用return + 返回结果
2、获得结果：变量 = 函数调用
"""

# 行后注释，代码后+2个空格+#+空格+注释

"""
此文件为测试文件，若想执行某个test文件，将第一行False 修改为True
"""

"""
缺省参数
gl_list = [1, 2, 3]
gl.list.sort() # 升序排序
gl_list.sort(reverse = True) # 若降序排序就得指定 reverse 参数，reverse = False是默认的缺省参数

定义默认参数的函数注意事项：
1、默认参数放在函数参数的末尾,
2、多个缺省参数的时候，在调用时候 缺省参数 = 来赋值 具体看下面print_info_test测试函数：

"""


def print_info_test(name, test, gender=True):
    """
    默认参数测试函数，默认参数放在函数参数的末尾，否则报错
    :param name:
    :param test:
    :param gender: 是否为男生，男生 True，女生 False
    :return:
    """
    if not test:
        return
    if not gender:
        print("%s是女生" % name)
    else:
        print("%s 是男生" % name)


print_info_test("LILei", False, True)
print_info_test("mary", False, gender=False)


"""
多值参数
有时候函数处理的参数个数不确定，这个时候可用多值参数
1、 参数前面加一个*，可以接受一个元组
2、 参数前面加2个*，则可以接受字典

"""


def mul_arg_test(num, test, *nums, **person):
    if not test:
        return
    print(num)
    print(nums)
    print(person)


# 元组和字典只需要用逗号隔开，下面2个调用效果是一样的
mul_arg_test(1, False, 1, 2, 3, 4, name="xiaoming",  age =18)
mul_arg_test(1, False, (1, 2, 3, 4), name="xiaoming", age =18)


"""
递归的函数定义
"""


def sum_test(number):
    if number == 0:
        return 0
    a = number + sum_test(number - 1)
    return a


test = False
if test:
    sum2 = sum_test(5)
    print("递归和 sum2=%d" % sum2)
"""
*****************************基本 函数的介绍和使用案例****************************************
"""


def type_test(test):
    """
    :param test: 是否执行测试
    :return:
    type 查看变量类型的测试函数
    """
    if not test:
        return
    g = 20
    print(type(g))


type_test(False)


def input_test(test):
    """
    :param test:
    :return:
     input 输入函数,控制台输入类型为str，若需要整数转化为int
    """
    if not test:
        return
    a = input("请输入数字")
    print(a)
    print(type(a))
    b = int(a)
    print(type(b))


input_test(False)

# 随机数
import random


def random_test(test):
    """
    :param test:
    :return:
    随机整数, 生成[1,10]中的随机数
    """
    if not test:
        return
    c = random.randint(1, 10)
    print(c)


random_test(False)


def id_test(test):
    """
    变量都是存储数值的内存地址，因此a ， b指向的地址都为1
    的地址
    :param test:
    :return:
    """
    if not test:
        return
    a = 1
    print(id(a))
    print(id(1))
    b = a
    print(id(b))


id_test(False)


"""
dir
python 中 变量、数据、函数都是对象

dir 内置函数传入 标识符/数据 可查看对象的所有属性以及方法

__方法名__ 格式是python提供的内置方法/属性


__new__     方法  创建对象的时候，会自动调用
__init__    方法  对象初始化的时候，自动调用
__del__     方法  对象被内存中销毁前，自动调用
__str__     方法  返回对象的描述信息，print函数输出使用

['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', 
'__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__',
'__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__',
'__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__']

"""


def dir_test_demo():
    """
    这是一个测试dir函数的demo函数
    """
    print("这是dir测试函数demo")


if False:
    # 查看所有内置函数
    print(dir(dir_test_demo))
    print(dir_test_demo.__doc__)


"""
eval 函数
将字符串当成有效表达式来求值，并返回结果
不要在input时候用eval转换
如：
input_str = input("请输入：")
print(eval(input_str))

若输入下面这行就可能会删除文件，不安全
__import__('os').system('rm 文件名') # 删除文件
__import__('os').system 相当与向终端送命令
"""
if False:
    s = "1 + 1"
    a = eval(s)
    print(a)
    b = eval("'--' * 10")
    print(b)
    # 字符串转化为列表
    lt = eval("[1, 2, 3]")
    print(lt)
    # 字符串转化为字典
    dic = eval("{'name': 'zs', 'age': 18}")
    print(dic)

