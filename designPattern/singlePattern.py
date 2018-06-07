"""
重写__new__方法，来实现单利模式的例子

原理： 类属性记住new返回的空间，若空间不空就返回 类属性
"""


class MusicPlayer(object):

    instance = None
    init_flag = False
    @classmethod
    def __new__(cls, *args, **kwargs):
        # 创建对象时，new方法会自动调用
        print("创建对象，分配空间 ！")
        # new 会为对象分配空间，并返回创建对象的引用，
        if MusicPlayer.instance is None:
            MusicPlayer.instance = super().__new__(cls)
            # 不返回则不会执行__init__
        return MusicPlayer.instance

    def __init__(self):
        if not MusicPlayer.init_flag:
            print("播放器初始化！")
            MusicPlayer.init_flag = True
        else:
            return

    @staticmethod
    def demo():
        print("demo")


# 会发现 3个播放器的内存地址一样，但初始化也执行了3次,因此添加类属性 init__flag来判断是否初始化过
# 若初始化过 则 直接返回
player1 = MusicPlayer()
player2 = MusicPlayer()
player3 = MusicPlayer()
if player1 is player2 and player2 is player3:
    print("1、2、3一样")

