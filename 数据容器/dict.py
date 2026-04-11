stuff_dict = {
    "Jake":{
        "部门":"科技部",
        "工资":3000,
        "级别":1
    },
    "Rose":{
        "部门":"市场部",
        "工资":5000,
        "级别":2
    },
    "Marry": {
        "部门": "市场部",
        "工资": 7000,
        "级别":3
    },
    "Mike": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "Bob": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}
print(stuff_dict)
for key in stuff_dict:
    if stuff_dict[key]["级别"] == 1:
        stuff_dict[key]["级别"] += 1
        stuff_dict[key]["工资"] += 1000
print("全体员工几级别为1的员工完成升职加薪后，数据为：")
print(stuff_dict)







