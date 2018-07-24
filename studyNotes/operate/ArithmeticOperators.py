# 加 +
a = 10 + 20
print(a)

# 减 -
b = 20 - 10
print(b)

# 乘 字符串乘法是连续的字符串拼接
c = 3 * 10
c2 = "-" * 5
print(c)
print(c2)

# 除 /  直接返回真实数据，可以为小数 下面结果返回0.5
d = 5 / 10
print(d)

# 取整数 返回除法结果的整数部分,返回为4
e = 9 // 2
print(e)

# 取余数
f = 9 % 2
print(f)

# 幂运算
g = 2 ** 3   # 2的3次方
print(g)

# 逻辑运算 and(并且)、or(或者)、not(否）
# and
c = 2 > 3 and 4 > 5
print(c)
# or
c2 = 2 > 3 or 4 > 3
print(c2)
c3 = not True
print(c3)

# 赋值运算符
c = a + b
c += 10  # 等同c = c + 10
c -= 10  # 等同c = c - 10
c *= 10  # 等同c = c * 10
c /= 10  # 等同c = c / 10


"""
 身份运算符
is 是判断2个标识符是不是引用的同一个对象
is not 与上面相反
== 判断的是引用变量的值是否相等（与java不一样）
"""


a = [1, 2, 3]
b = [1, 2]
b + [3]
print(a)
print(b)
if b is a:
    print("a 和 b 是同一个对象")
else:
    print("a 和 b 不是同一个对象")

if b == a:
    print("a 和 b 值是相等的")
else:
    print("a 和 b 值是不相等的")
