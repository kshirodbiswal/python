# ! list: list is a data type in python to store multiple values.(like array)
# * the main diff between array and list  is  that array stores data in continuos memory allocation but in list there is no direct continuos memory allocation.
# * list can be heterogenius but  traditional arrays are homogenious only(i.e. that can store only similar type of value)


# !1.creating list:
l=[10,2,"hello",True,3.2,"hii"]
print(l)

# multi-dimensional list
# 2d list
l2=[10,20,3,[10,20,30,"hello"]]
print(l2)
# 3d list
l3= ["hello",32,3.2,["hello",2,30,["hii",10,20,30]]]
print(l3)
# list creating by type function
l4=list("hello")
print(l4)
# empty list
l5=list()
print(l5)

# !2. Accessing item from a list
print(l[3])
print(l[-1])
print(l[1:3])
print(l[::-1])
# in 2d list
print(l2[3][-1])
# in 3d list
print(l3[3][3][0])
# !3.edit item in list
l=[1,2,3,4,5]
l[-1]=500
l[0]=100
print(l)
l[1:4]=[200,300,400]
print(l)

# ! 4.add items in list
# append:try to add one item
l.append(1000)
l.append([5,6])
print(l)
# extend: try to add multiple item
l.extend([5000,6000,7000])
l.extend("goa")
print(l)
# insert:you can add items in pecific index position 
l.insert(2,"hii")
print(l)
# !5.delete item from a list
# del
del l5  #delete entire list
# print(l5)
del l[2]#delete a item
print(l)

# remove:specify item to remove insted of index position
l.remove([5,6])
print(l)
# pop:delete the last item
l.pop()
print(l)
# clear:make list empty
l.clear()
print(l)

# !6.list operations
l=[1,2,3,4]
l1=[5,6,7,8]
print(l+l1)
print(l*3)
for i in l:
    print(i)
print(2 in l)

# !7.list functions
print(len(l))
print(min(l))
print(max(l))
print(sorted(l,reverse=True))#it does not make chaange in original list it will create a new list
print(l)
l.sort(reverse=True)#it  make chaange in original list it will create a new list
print(l)
print(l.index(3))
