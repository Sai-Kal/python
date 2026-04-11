#建立一个学生列表
student_age = [21,25,21,23,22,20]
#在尾部插入31
student_age.append(31)
#在尾部插入一个新列表
new_list = [29,33,30]
student_age.extend(new_list)
print(student_age)
#取出第一个元素
one = student_age.pop(0)
print(one)
#取出最后一个元素
two = student_age.pop(-1)
print(two)
#查找元素31的下标
index = student_age.index(31)
print(index)
print(student_age)