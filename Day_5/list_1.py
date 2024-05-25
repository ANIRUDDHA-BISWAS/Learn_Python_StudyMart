# list
# index value start from ZERO [0,1,2,3]

# INDEX  0  1   2   3   4   5   6   7   8   9
# list1  15 20  25  30  35  40  45  50  55  60
# INDEX  -9 -8  -7  -6  -5  -4  -3  -2  -1  0

list1 = [15,20,25,30,35,40,45,50,55,60]
print(list1[1])
print(list1[-1])
print(list1[2:6])
print(list1[2:])
print(list1[:6])
print(list1[:])
print(list1[::])
print(list1[-2:-6])
print(list1[-6:-2])

# element add
list1.append(65)
print(list1)

# element insert
list1.insert(3,27)
print(list1)


# new list
list2 = [70,75,80]

list1.extend(list2)
print(list1)


list2.extend(list1)
print(list2)