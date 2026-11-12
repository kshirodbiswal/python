# ! touple are immutable in nature
# ! tuples are read only data type
# !1.creating a tuple
t1=() #empty tuple
print(t1)
t2=(1,2,4,71)
print(t2)
t3=(1,2,4,71,(2,4))#2d tuple
print(t3)
t4=(7,) #single value tuple : to create a single value tuple use comma at lat  if not then it will become  the original type not a tuple.
print(type(t4))
t5= tuple("hello")

# ! acceing a tuple:
print(t2[1])
print(t3[4][1])

# ! we cannot edit or add to a exiting tuple and deleting a item from touple as it is immutable like string. we can delete the entire tuple.

# !2.operation on tuple
print(t2+t3)
print(t2*2)
for i in t2:
    print(i)
print(1 in t2)

# !3.function
print(len(t2))
print(min(t2))
print(max(t2))
print(sum(t2))
print(sorted(t2))
print(sorted(t2,reverse=True))
