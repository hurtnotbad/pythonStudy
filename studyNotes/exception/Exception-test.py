"""
异常：编写的代码符合语法，但运行时出现错误

捕获异常：不确定执行的代码会否出现异常，就需要捕获
grammar：
try：
    不确定是否会出错的的代码
except error1:
    出现错误的处理
except error2:
    出现错误的处理
except (error3, error4):
    出现错误的处理
except Exception as result:
    print(result)
else:
    没有异常才会执行的代码
finally:
    无论是否有异常，都会执行

"""


def exception_test(test):
    """
    捕获已知异常
    :param test:
    :return:
    """
    if not test:
        return
    try:
        num = int(input("exception_test请输入整数："))
        result = 8/num
        print(result)
    except ValueError:
        print("请您输入正确的整数:")
    except ZeroDivisionError:
        print("除数应该不等于0的数")


exception_test(False)

"""
捕获未知异常
开发中如果无法预测所有可能出现的错误，因此 增加一个except，语法如下：
except Exception as result:
    print("未知错误 %s" % result)
    
因此一般在捕获异常的时候，最后面加上 未知错误 的捕获
"""


def unknown_exception_test(test):
    """
    捕获已知异常，若输入了0 则判定为未知错误
    :param test:
    :return:
    """
    if not test:
        return
    try:
        num = int(input("unknown_exception_test 请输入整数："))
        result = 8/num
        print(result)
    except ValueError:
        print("请您输入正确的整数")
    except Exception as result:
        print("未知错误 %s" % result)


unknown_exception_test(False)

"""
***********************异常的传递：********************

当函数/方法 执行出现异常，就会将异常传递格尔 函数/方法的调用一方，若果传递到主程序，仍然没有处理异常，程序才会终止
"""


def demo1():
    return 2/0


def ex_pass_test(test):
    if not test:
        return
    # 执行demo1出错，传递异常到print ，print没有异常处理，就会终止,
    # 利用异常传递性可以在主程序里捕获异常
    try:
        print(demo1())
    except Exception as result:
        print(result)


ex_pass_test(True)

"""
**********************抛出异常，业务需求自己手动抛出异常*********
当设置密码的时候要求长度大于8 或者必须为6位，否则不符合规范，这时候就得手动抛出异常，或者弹提示框

手动抛出异常后，程序运行就会出错
"""


def raise_exception_test(test):
    if not test:
        return
    pwd = input("请输入密码：")

    if len(pwd) >= 8:
        print("输入密码格式正确")
        return pwd
    ex = Exception("密码长度不够")
    raise ex
    

# 手动抛出异常后，程序运行就会出错，我们可以在主程序里面捕获，则会输出 抛出异常的描述信息
raise_exception_test(False)
