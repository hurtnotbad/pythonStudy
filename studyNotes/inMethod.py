"""
内置方法介绍，内置方法是object 基类提供的 内置 静态方法

"""

"""
__new__ 方法
使用类名创建对象，解释器调用 __new__对象分配空间
__new__ 主要2个作用
1、内存中为对象分配空间
2、返回 对象的引用
解释器获得对象的引用后，将引用作为第一个参数，传递给__init__方法
"""


class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        # 创建对象时，new方法会自动调用
        print("创建对象，分配空间 ！")
        # new 会为对象分配空间，并返回创建对象的引用，
        instance = super().__new__(cls)
        # 不返回则不会执行__init__
        return instance

    def __init__(self):
        print("播放器初始化！")


new_test = False
if new_test:
    player = MusicPlayer()
