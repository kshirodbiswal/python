# ! dictionary:It is a special data type stores in a key value pair.
# ! rules of dictionary:
# !1.Dictionary has no indexing.
# !2.Dictionary is a mutable type.
# !3.keys->immutable,values-> can be mutable 
# !4.keys should be unique


# ! mutable:which can change in same memory address , immutable :which cannot change in same memory address.
# !mutable type: list,sets,dictionary
# !immutable:int,float,boolean,string,tuple,complex


# !1.creating dictionary
d={}
print(d)
d={"name":"raja","age":20}
print(d)
d1={(1,2,3):"hello"}  #key are always immutable
print(d1)
d2={"name":"rahul","name":"rohit"} #if we use same key multiple time then it keep only last updated one
print(d2) 
# 2d dictionary
d3={"name":"raja","school":"pkv","mark":{"s1":70,"s2":80,"s3":90}}
print(d3)

# !2.accesing item from  dictionary : there i only one way to acces item from dictionary i.e. by providing the key as there is no indexing.
print(d["name"])  
print(d["age"])
print(d3["mark"]["s2"])

# !3.editing in dictionary
d["name"]="rajaa"
d["age"]=22
print(d)
# !4.add new key value pair
d["gender"]="male"
print(d)
# !.delete in dictionary
del d["gender"]
print(d)
d1.clear() #make it empty
print(d)

# !operation
for i in d:
    print(d[i])

print("rajaa" in d) #memberhip check in keys

# !function:
print(len(d))
print(min(d))
print(max(d))
print(d.keys())
print(d.values())