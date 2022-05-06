def method_1():
    # 用户身份验证
    username = input('用户名：')
    password = input('密码：')
    if username == 'admin' and password == '123':
        print('身份验证成功')
    elif username == 'admin' and password != '123':
        print('密码错误')
    else:
        print('身份验证失败')


def method_2():
    # 分段函数求值1
    x = float(input('x = '))
    if x > 1:
        y = 3 * x - 5
    elif x >= -1:
        y = x + 3
    else:
        y = 5 * x + 1
    print('func(%.2f) = %.2f' % (x, y))


def method_3():
    # 分段函数求值2
    x = float(input('x = '))
    if x > 1:
        y = 3 * x - 5
    else:
        if x >= -1:
            y = x + 3
        else:
            y = 5 * x + 1
    print('func(%.2f) = %.2f' % (x, y))


def method_4():
    # 英制单位英寸和公制单位厘米互换
    value = float(input('请输入长度：'))
    unit = input('请输入单位：')
    if unit == 'in' or unit == '英寸':
        print('%f英寸 = %f厘米' % (value, value * 2.54))
    elif unit == 'cm' or unit == '厘米':
        print('%f厘米 = %f英寸' % (value, value / 2.54))
    else:
        print('请输入有效的单位')


def method_5():
    # 百分制成绩转化为等级制成绩
    score = float(input('请输入成绩：'))
    if score >= 90:
        grade = 'A'

    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'E'
    print('成绩等级为：', grade)


def method_6():
    # 输入三边长，如果能构成三角形就计算周长和面积
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    if a + b > c and a + c > b and b + c > a:
        print('周长：%f' % (a + b + c))
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print('面积：%f' % area)
    else:
        print('三边[a=%.2f, b=%.2f, c=%.2f]不能构成三角形' % (a, b, c))


# method_1()
# method_2()
# method_3()
# method_4()
# method_5()
method_6()
