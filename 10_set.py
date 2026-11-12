# !rules of sets:
# !1.sets do not allow duplicate value.
# !2.sets have no indexing/slicing.
# !3.sets do not allow mutable datatypes.
# !4.set itself is a mutable datatype. so there is not possible to create a multidimentional sets.

# !1.creating set:
s1 = {} # it will create a  dictionary not a empty set. a both dictionary and set use {} but default choice is dictionary by python.
print(type(s1))
s1= set() #it is create a empty set.
print(type(s1))
s1={1,2,3,4}#homogenious: same datatype
print(s1)
s2={1,2,3.2,"hello",True}#heterogenious: diff datatype
print(s2)
s3={1,2,3,3,2,1,4}
print(s3)
s4={(1,2,3),"hello"}
print(s4) #*while printing the order of s4 is changed it is bcz set donot have any indexing they uses hasing.

# ! we cannot acces set  items using indexing as  there is no index in set and so cannot edit the set but we can add,delete items in set.


print(id(s1))
s1.add(5)
print(s1)
print(id(s1))
s1.remove(5)
print(s1)
s1.pop() #instead of remove from  right it remove from left in set bcz of hasing. 
print(s1)
# ! so set is a mutable datatype where we can add,delete  but not edit.

# !2.set operation: only looping and membership operator working concating,multiplying not working.
for i in s1:
    print(i)

print(3 in s1)

# !3.functions
print(len(s1))
print(min(s1))
print(max(s1))
print(sum(s1))
print(sorted(s1,reverse=True))

# set specific function
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))
print(s2.symmetric_difference(s1))
print(s2.isdisjoint(s1))
print(s1.issubset(s2))
print(s1.issuperset(s2))