import keyword
"""
关键字是python内置的、具有特殊意义的标识符，可通过print(keyword.kwlist) 查看所有关键字有如下：
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class',
 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 
 'while', 'with', 'yield']
 
 关键字在使用时不需要括号，例：
 a = ["a", "b", "c"]
 del a[0]
 就可以删除a列表中第一个元素 

"""


def show_keyword_test(test):
    """
    查看所有关键字
    :param test:
    :return:
    """
    if not test:
        return
    print("keyword:")
    print(keyword.kwlist)


show_keyword_test(True)