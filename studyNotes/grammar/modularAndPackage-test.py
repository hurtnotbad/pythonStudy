"""
模块化：python 程序架构的一个核心概念

1、每一个py结尾的python源码文件都是一个模块
模块名同样也是一个标识符，需要符合标识符的命名规则
在模块中第一的全局变量、函数、类都是提供给外界直接使用的工具
模块好比工具包，要想使用工具包工具，需要先导入模块

导入方式
1、import 导入 grammar：将模块中变量、类等一次性全部导入
import 模块名1，
import 模块名2

导入后，通过 模块名. 来使用变量、函数、类

as
当导入的名字太长，则可以用过as 制定名称，方便代码中使用

from
1：可以直接导入模块的类、全局变量
grammar：
from 模块名 import 工具名
1、在使用工具名就不需要使用模块名
2、如果from从2个模块中导入 同名的函数，那么后导入的模块函数会覆盖先导入的函数

form 模块名1 import *
这种方式导入模块1所有工具，在使用工具的时候不需要模块名（不推荐使用）

"""

# 可以正常使用，但为什么报错还不清楚
import studyNotes.method.inMethod as inMethod

if True:
    p = inMethod.MusicPlayer()



"""
******模块搜索顺序

1、 搜索当前目录 指定的模块名文件，如果有就导入
2、 如果没有，再搜索系统目录（因此开发时候，模块名不要和系统模块名重名）

python中每个模块都有一个内置属性 __file__ 可以查看模块的完整路径

python中每个模块都有一个内置属性 __name__
在导入模块中，若没有缩进的代码都会执行，而实际开发，每个模块独立开发，会有部分测试代码，而测试代码希望：
仅在模块内部使用，而被导入时不执行
__name__ 是python的一个内置属性，记录着一个字符串，
1、若被其他文件导入的，__name__就是一个模块名
2、若是当前执行的程序，则__name__是__main__

因此在测试代码中加入：
if __name__ == "__main__":
    test 代码 
"""
if True:
    print(__file__)
    print(__name__)


"""
包：
1、包含多个模块的特殊目录
2、目录下包含一个特殊的文件 __init__py
3、包的命名方式和变量名一致，小写字母+_

import 包名
好处，导入包就相当于把所有的模块都导入了。

在 __init__文件中添加各个模块，格式如下
from . import 模块名称

"""

"""
*********************发布模块**************
制作发布压缩包

1、 创建setup.py
setup.py文件
from distutils.core import setup

setup(name="lammy_study",  # 包名
      version="1.0",  # 版本
      description="这是一个测试包",  # 描述信息
      long_description="完整的描述",  # 完整描述信息
      author="lammy",  # 作者
      author_email="1181942612@qq.com",
      url="www.itheima.com",  # 主页
      py_modules=["class_study", "DataType"])  # 输入要打包进去的模块
    
2、 构建模块,
    可以在pycharm Terminal直接输入：python setup.py build
    ubantu 下 输入$ python3 setup.py build
    
    执行完后回在当前目录生成build目录，会在build/lib下看到要打包进去的模块

3、生成发布压缩包
    可以在pycharm Terminal直接输入：python setup.py sdist
    ubantu下 $ python3 setup.py sdist
    
    执行完后回在当前目录生成dist目录，会在此目录下看到生成的.gz包
    

4、安装模块，他人拿到分享的压缩包
ubantu： sudo python3 setup.py install
安装后就可以 import 压缩包的模块了

5 卸载模块
cd 到安装的目录

import 包名
print(包名.__file__)查看完整路径
rm -r 包名*
删除安装的包
"""