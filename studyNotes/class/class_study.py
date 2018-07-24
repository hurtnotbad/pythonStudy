"""
类(class)
语法格式：第一个参数是self

class name：
    def function1(self, 参数列表)：
        执行语句

    def function1(self, 参数列表)：
        执行语句

"""


class Cat:

    def eat(self):
        print("吃鱼")
        self.drink()

    def drink(self):
        print("喝水")


test_1 = False
if test_1:
    tom = Cat()
    tom.eat()
    tom.drink()
    # 输出tom对象的地址
    print(tom)

"""                      
**********************给类对象增加属性**********************
    这种方式不推荐使用
"""
test_2 = False
if test_2:
    tom2 = Cat()
    tom2.name = "Tom2"
    # print(tom.name) # 会报错，因为tom 没有name属性，因此，在外面添加属性会存在这样的隐患,在初始化方法中添加属性
    print(tom2.name)

"""
***********************类创建过程*****************************   
1、 为对象在内存中分配空间  -- 创建对象
2、为对象属性 设置初始值    -- 初始化方法（init）,类似java的构造函数
这个初始化方法就是 __init__方法，__init__ 是对象的内置方法
3、对象要在内存中销毁前，自动调用__del__方法
"""

"""
***********************类的init为对象增加默认属性*****************************   
"""


class Cat2:

    def __init__(self):
        print("初始化方法")
        self.name = "Tom"


add_test = False
if add_test:
    l_tom = Cat2()
    print(l_tom.name)
    l_tom.name = "tom2"
    print(l_tom.name)


"""
***********************类的init增加参数*****************************   
类似java的构造函数，为类添加属性，和为属性赋值参数的值
"""


class Cat3:

    def __init__(self, name):
        print("初始化方法")
        self.name = name


test3 = False
if test3:
    tom3 = Cat3("tom3")
    print(tom3.__doc__)


""" 
***********************类的私有方法，私有属性*****************************   
类的私有属性和私有方法是在属性或方法前面加2个下划线：
__方法名
__属性名

python对类私有只是进行的特殊处理，用 _类名__属性/方法：实际开发中不要使用
"""


class Cat4:

    def __init__(self, name):
        print("初始化方法")
        self.__name = name

    def __secret(self):
        print("这是私有方法")

    def p_say(self):
        print("name = %s" % self.__name)
        self.__secret()


test4 = False
if test4:
    tom4 = Cat4("tom4")
    # print(tom4.__name)  # 此句会报错，找不到属性名 __name
    # tom4.__secret()  # 报错 object has no attribute '__secret'
    tom4.p_say()
    # python对类私有只是进行的特殊处理，用 _类名__属性/方法：实际开发中不要使用
    print(tom4._Cat4__name)
    tom4._Cat4__secret()


"""
****************************继承**********************************
单继承
class 类名(父类名):
    ...
    ...

如下面： Dog类是Animal的子类/派生类，相反Animal是Dog类的父类/基类

继承的传递性： 子类拥有父类以及父类的父类中封装的所有方法， 但不具备父类的私有方法/属性，因此下面的调用是错误的
"""


class Animal:

    def eat(self):
        print("eat")

    def drink(self):
        print("eat")

    def run(self):
        print("eat")

    def sleep(self):
        print("eat")

    def __haha(self):
        print("haha")


class Dog(Animal):
    def bark(self):
        print("汪 汪 汪")
        # 子类拥有父类以及父类的父类中封装的所有方法， 但不具备父类的私有方法/属性，因此下面的调用是错误的
        # self.__haha()


test5 = False
if test5:
    dog = Dog()
    dog.eat()
    dog.bark()


"""
**************** 覆写 扩展 父类方法******************************
覆写： 定义和父类一样的方法
扩展： 1、定义和父类一样的方法，
       2、调用super().父类方法，然后继续特有的操作
"""


class XiaoTianQuan(Dog):
    """
    覆写父类方法
    """
    def bark(self):
        print("叫的神一样")


class XiaoTianQuan2(Dog):
    """
    扩展父类方法
    """

    def bark(self):
        super().bark()
        print("叫的神一样")


test5 = False
if test5:
    dog2 = XiaoTianQuan2()
    dog2.bark()


"""
**************************** 多继承 ********************************
python 是可以多继承的
grammar：
class 字类名(父类名1， 父类名2， ...):
    pass

注意事项：
1、若父类之间有相同的函数的时候，尽量不要多继承

MOR
python 中的mro (method resolution order) 方法搜索顺序
python 中针对类提供一个内置属性 __mro__ 可以查看方法搜索顺序
MOR主要用于多继承时判断方法、属性的调用路径

"""


class A:

    def test(self):
        print("A --- test")

    def demo(self):
        print("A --- demo")

class B:

    def demo(self):
        print("B --- demo")

    def test(self):
        print("B --- test")


class C(A, B):
    pass


# 多继承，当父类设计相同函数的时候，可以查看mro信息，来判断是用A的方法还是用B的方法
test5 = False
if test5:
    # 查看mor顺序，根据顺序找，找到了就执行，没找到才会找后面的，最后object类中找，object是左右类的基类
    print(C.__mro__)
    print(C.mro())
    # 打印的顺序：[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
    # 在c中没找到就去A -B - Object顺序找
    c = C()
    c.test()
    c.demo()


"""
*********************python新式类与旧式类********************
object类是python所有对象的基类，提供有一些内置属性和方法，可用dir查看

新式类： 以object类为基类的类，推荐使用
经典类： 不以object类为基类的类，不推荐使用

python3 中定义类，若无指定父类 ， 会默认以object为该类的基类-- python3中定义的类都是新式类
python2 中则不会

新式类和经典类在多继承时候，会影响到方法的搜索顺序
为了保证程序的兼容性，在用python2和3都可以运行，在定义类时若没有父类，建议统一继承自object类
例：
class A(object):
    pass
"""


""" 
********************多态************************
多态 不同的字类对象调用相同的父类方法，产生不同的执行结果
1、增加代码的灵活性
2、以继承和重写父类为前提
3、调用方法技巧，不会影响到类的设计

如下面的例子，人听到动物的叫声，根据传入的动物不同，调用不同的叫声
"""


class Animal:

    def shout(self):
        # print("叫叫叫")
        return "叫叫叫"


class Sheep(Animal):
    def shout(self):
        # print("mie mie mie")
        return "mie mie mie"


class Cow(Animal):
    def shout(self):
        # print("mie mie mie")
        return "ma ma ma"


class Person:

    def hear(self, animal):
        # 调用父类 animal的shout（） 方法，根据传入的animal的对象不同，执行不同的方法
        print("我听到了叫声 %s" % animal.shout())


test6 = False
if test6:
    sheep = Sheep()
    cow = Cow()
    person = Person()
    person.hear(sheep)
    person.hear(cow)


"""
******************** 类 在内存的存在和 类是一个特殊对象***************
python 和java一样一切皆对象
class AA:  定义的类属于 类对象
python中类是一个特殊的对象----类对象
obj = AA() 属于  实例对象

1、程序运行时：类同样会被加载到内存，
2、python中，类是一个特殊的类对象
3、程序运行时，类对象在内存中只有一份，使用一个类可以创建多个对象实例
4、除了封装 实力的属性和方法外，类对象还可以拥有自己的属性和方法

简单的说：类对象内存只有一份，而每个实例对象共用类对象的方法，在使用时将自己当作参数传入方法，调用自己的实例对象的属性，完成各自的操作，内存中拥有实例对象各自的属性
"""


"""
******************************类属性定义和使用************
类属性： 就是在类对象中定义的属性
1、通常记录与这个类相关的特征
2、类属性不会用于记录具体对象的特征
class 类名：
    属性 = 值
    pass
例子如下面

若想给具体的类的属性，则在init添加属性，并赋值（如java的构造函数一样）
类属性则如同java的static方法一样，属于类对象的属性，非具体实例类的属性
"""

"""
**************************属性的获取机制******************
属性获取向上获取：
现在类对象中寻找该属性，若有就输出，若没有就在类对象中找，找到了就输出

在访问和设置 类属性的时候用 类名，不要用具体的对象.属性名，因为，这样会为具体的类对象增加属性，而不是为类增加属性，下面例子
输出count工具的总数的时候就出现问题
"""

class Tool(object):

    count = 0
    name = "工具名称"

    def __init__(self, name):
        Tool.count += 1
        self.name = name


test6 = False
if test6:
    tool1 = Tool("斧头")
    tool2 = Tool("锄头")
    tool3 = Tool("水桶")
    # Tool 中有name 就返回 Tool name
    print(Tool.name)
    # tool1 实例中有name 则返回tool1的名字 斧头
    print(tool1.name)
    # Tool类对象中有count 则直接返回count属性
    print(Tool.count)
    # tool1 实例中没有count 则向上寻找类对象的属性名 count
    print(tool1.count)

    # 下面一句，是在tool1 类找属性count 没有，若没有则给tool1 增加count属性，不会向上寻找类的属性值count，因此没有修改类属性
    tool1.count = 99
    print("工具数:tool1.count = %d" % tool1.count)
    print("工具数:Tool.count = %d" % Tool.count)


"""
*****************************类方法*************
类方法：不需要访问实例对象的属性 只访问类属性时候用（如android static方法类似，只能访问static变量）
类属性：就是针对类对象的属性
    使用赋值语句在class关键字下方 定义类属性
类方法：就是针对类对象定义的方法
    在类方法内部可以直接访问类属性或者调用其他类的方法

grammar：
@classmethod
def 类方法名(cls):
    pass

1、 需要@classmethod 修饰器，告诉解释器这是一个类方法
2、类方法的第一个参数cls
    由哪一个类调用的方法，方法内的cls 就是一个类的引用
    这个参数和实例方法的第一个参数是self类似
    提示使用其他的名称也可以，不过习惯使用cls
3、通过类名，调用类方法，调用方法时，不需要传递参数cls
4、在方法内部
    可以通过cls 访问类的属性
    可以通过cls 调用其他的类方法
"""


class Tool2(object):

    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具的总数：%d" % cls.count)

    def __init__(self, name):
        Tool2.count += 1
        self.name = name


test7 = False
if test7:
    tool1 = Tool2("斧头")
    tool2 = Tool2("锄头")
    tool3 = Tool2("水桶")
    Tool2.show_tool_count()


"""
*********************静态方法*********************
静态方法：当方法
    1  不需要访问实例属性 或者 实例方法 
    2、不需要访问 类属性 或者 类方法(可以通过类名+方法/属性访问)
就可以把这个方法定义成静态方法,静态方法可以互相调用

静态方法语法：
@staticmethod
def 静态方法名():
    pass

1、@staticmethod 修时器
2、通过类名.调用静态方法

下面的例子，若 不用@staticmethod ， 会弹出 提醒使用 静态方法的警告
"""


class Dog3(object):

    name = "dog"

    @classmethod
    def eat(cls):
        print("eat")

    @staticmethod
    def run():
        print("%s跑" % Dog3.name)
        Dog3.eat()


test8 = False
if test8:
    Dog3.run()
