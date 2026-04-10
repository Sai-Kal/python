print("----------------------------主菜单---------------------------")
money = 5000000
name = input("请输入您的姓名：")
def balance():
    print("---------------查询余额----------------------")
    print("{}，您好，您的余额剩余：{}元".format(name, money))

def deposit(x):
    print("---------------存款----------------------")
    global money
    money = money + x
    print("{},您好，您存款{}元成功,您的余额为{}".format(name, x,money))

def withdraw(y):
    print("---------------取款----------------------")
    global money
    money = money - y
    print("{},您好，您取款{}元成功,您的余额为{}".format(name, y,money))

def menu(num):
    if num == 1:
        balance()
    elif num == 2:
        x = int(input("请输入存款金额："))
        deposit(x)
    elif num == 3:
        y = int(input("请输入取款金额："))
        withdraw(y)
    elif num == 4:
        print("----------------退出系统--------------")
        return True

while True:
    choice = int(input("{}，您好，请选择操作：".format(name)))
    if menu(choice):
        break
