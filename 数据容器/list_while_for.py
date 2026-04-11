#while循环
def while_func():
    num_list = [1,2,3,4,5,6,7,8,9,10]
    new_list = []
    index = 0
    while index < len(num_list):
        if num_list[index] % 2 == 0:
            element = num_list[index]
            new_list.append(element)
        index += 1
    print(new_list)
while_func()

#for循环
def for_func():
    num_list = [1,2,3,4,5,6,7,8,9,10]
    new_list = []
    for element in num_list:
        if element % 2 == 0:
            new_list.append(element)
    print(new_list)

for_func()



