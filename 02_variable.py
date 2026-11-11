# python has no variable declaration bcz it has dynamic typing
# Dynamic typing: the datatype of a variable is decided in the runtime. we donot need to specify it.
name = "hitesh"   # it is dynamic typing
print(name)

# It support Dynamic binding
# Dynamic Binding:  changing the datatype of a variable  is sopported
name= True #It is dynamic binding
print(name) 

# multiple variable declaration in a single line
a=4;b=5;c=6;
print(a,b,c)
a,b,c =10,20,30
print(a,b,c)
a=b=c=30
print(a,b,c)

# taking input from user
name = input("Enter name:") # this function takes input in STRING format you have to convert it to your required type.
print("hello ",name)
age = input("Enter age:")
print("age is ",age)
type(age)

# type conversion : converting one datatype to another datatype
# 1.implicit typeconversion : it isss done by the  compiler
print(4+3.5)
# 2.explicit type conversion: it is done by us progrmmer.
age= int(age)
print(type(age))
# note : type conversion is only happen if the data type is compatable
