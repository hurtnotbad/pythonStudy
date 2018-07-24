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
