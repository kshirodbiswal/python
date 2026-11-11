# !built-in functions: the functions which are already there by python  we just call it by passing argument and use it

# 1.print
print("hello")
# 2.input: the value recieve from input function  is string type 
print(input("enter name:"))
# 3. type:return the data type of a given value
print(type(4.2))
# 4. type conversion function : int,str,float,list,touple etc.
print(int(6.4))
# 5. power: return power of no
print(pow(2,3))
# 6.min/max : return the min/max value of a itterable(string,list,touple) type.
print(min("hello"))
print(max([10,20,34,5]))
# 7.divmod: return division and modulos of two no in a touple
print(divmod(5,2))
# 8. bin/oct/hex : returns binary/octal/hexadecimal values
print(bin(2))
print(oct(2))
print(hex(2))
# 9. id: return the meory address of  input
print(id(4))
# 10.ord: return ascii value of a charecter
print(ord('A'))
# 11.len: return  the length  of itterable
print(len("hello"))
# 12.sum: return the sum value of itterables
print(sum([1,2,10,45]))
# 13.help: if you want to read documentation of a function pass it in help.
# help('modules')

# !built-in-modules: modules are the file containg  a set of  functions  we can usee in our program.
# e.g. math,random,os etc..
import math;
print(math.pi)
print(math.ceil(4.7))
print(math.floor(4.2))
import random
print(random.randint(1,100))
a= [10,20,30,6,8,9]
print(random.shuffle(a))
import time
print(time.ctime()) 
time.sleep(1)
print("hello")
import os;
print(os.getcwd())
print(os.listdir())
