balance = 10000;
for i in range(1,21):
    import random;
    num = random.randint(1,10);
    if num <= 5:
        print(f"员工{i}，绩效{num}，低于5，不发工资，下一位")
        continue;

    else:
        if balance < 0:
            print("工资发完了，下个月领取")
            break;
        else:
            balance = balance - 1000;
            print(f"向员工{i}发工资给1000元，账户余额还剩余{balance}元");
