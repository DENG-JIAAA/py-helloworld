import math


def method_one():
    # 使用变量保存数据并且进行加减乘除运算
    a = 321
    b = 123
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)

    # 使用type()函数来检查变量的类型
    x = 'hello'
    y = True
    print(type(x))
    print(type(y))
    print(type(type(y)))
    # python内置函数
    print(ord('c'))
    print(chr(99))
    i = int(input('i = '))
    j = int(input('j = '))
    print('%d + %d = %d' % (i, j, i + j))
    print('%d - %d = %d' % (i, j, i - j))
    print('%d * %d = %d' % (i, j, i * j))
    print('%d / %d = %d' % (i, j, i / j))
    print('%d // %d = %d' % (i, j, i // j))
    print('%d %% %d = %d' % (i, j, i % j))
    print('%d ** %d = %d' % (i, j, i ** j))
    print(type(3 / 1))
    print(type(3 // 1))
    print(type(3.0 // 1))
    print(type(3 // 1.0))


def method_two():
    a = 10
    b = 2
    a += b
    a *= a + 2
    print('a =', 4, ', b =', 5)


def method_three():
    """
    华氏温度转换为摄氏温度
    转换公式为：$C=(F - 32) \div 1.8$
    """
    f = float(input('请输入华氏温度：'))
    c = (f - 32) / 1.8
    print('%.1f（华氏度） = %.1f（摄氏度）' % (f, c))
    print(f'{f:.1f}（华氏度） = {c:.1f}（摄氏度）')


def method_four():
    """
    计算圆周长和面积
    """
    r = float(input('请输入圆半径：'))
    perimeter = math.pi * r * 2
    area = math.pi * r * r
    print('周长：%.2f' % perimeter)
    print('面积：%.2f' % area)


# method_one()
# method_two()
# method_three()
# method_four()


# 输入年份判断是不是闰年
year = int(input('请输入年份：'))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)
