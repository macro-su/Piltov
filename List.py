#!/usr/bin/python3

list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
list1[3] = "baidu"
print(list1)

del list1[1]
print(list1)

for x in list1:
    print(x, end="")