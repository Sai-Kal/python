print("-------------函数的传入参数------------------")
# 函数的传入参数
def add(x,y):
    result = x + y;
    print("{} + {}的结果是：{}".format(x,y,result));
add(1,2)



print("------------------练习---------------------")
def temp(x):
    print("请出示你的健康码以及72小时核酸证明，并配合测量体温！");
    if x > 37.5:
        print("您的体温是{}，需要隔离".format(x));
    else:
        print("您的体温是{}，体温正常请进".format(x));
temp(36.5)

print("------------------函数的返回值--------------")
# 函数的返回值
#定义
def add(x,y):
    return x + y
sum = add(5,6)
print(sum)
print("------------------None类型-------------------")
#None类型
#用在函数无返回值上
def name():
    print("My name is Jake")

result = name()
print("无返回值函数，返回内容是：{}".format(result))
print("无返回值函数，返回内容类型是：{}".format(type(result)))
print("------------------None用在if判断里------------------")
#用在if判断上，None相当于false
def age(num):
    if num < 18:
        return None
    else:
        return "Success"
def check():
    if not result:
        print("未成年不能进入")
    else:
        print(result)

result = age(15)
check()
result = age(19)
check()


# 用于声明无初始内容的变量


print("---------------函数的说明文档--------------------")
# 函数的说明文档
def add(x,y):
    """
    add函数可以接收2个值，并对其进行加法运算
    :param x: 形参x.....
    :param y: 形参y.....
    :return: 返回形参x和形参y相加的结果
    """
    result = x + y
    print("{} + {} = {}".format(x,y,result));
    return result
add(5,6)



print("---------------函数的嵌套调用-------------")
# 函数的嵌套调用
def func_b():
    print("---2---")
def func_a():
    print("---3---")
    func_b()
    print("---4---")

func_a()

print("--------------变量---------------------")

print("--------------局部变量-------------------")
# 变量在函数中的作用域
# 局部变量：定义在函数体内部的变量，只在函数体内部生效，临时保存数据
def testA():
    num = 100
    print(num)
testA()


print("------------全局变量------------")
# 出了函数体，无法使用
# print(num)
# 全局变量
num = 200
def testB():
    print("testB:{}".format(num))

testB()
print(num)

print("------------global关键字-----------")
# global关键字

num = 300
def testA():
    print("testA:{}".format(num))
def testB():
    num = 500  #局部变量
    print("testB:{}".format(num))
def testC():
    global num
    num = 888
    print("testC:{}".format(num))

testA()
testB()
testC()
print(num)









