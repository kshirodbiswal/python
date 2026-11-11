# ! string: it iss the sequence of charecters 
# ! in python strings are a sequence of unicode charecters.

#!1. creating a string: 
string = "hello world"
print("hii i'm abhijit")
uid=101
name = str("raaja")

# accesing a sub string from a string
# *indexing: getting the index value from a sequence of string.
# type of indexing: 
# 1.positive indexing : left to right
print(string[2])
# 2.negative indexing: right to left
print(string[-1])

# *slicing: extracting a sub string from  a string 
print(string[0:5])
print(string[0:5:2]) # get char in range 0 to 5 in 2 skips
print(string[::-1]) #  reversed string  it can applicable on all itterables.

#! 2. edit  and deleting a string
# * string is a immutable data type so we cannot edit a string and delete a part of string .
# * we can replace the entire string  and delete the entire string by using del function.
s= "hello"
print(s)
s="hii"
print(s)
del s
# print(s)

#! 3.operations on string:
#* i.arithematic operator
print("hello"+" hii")
print("a"*10)

#* ii.relational operator
print("hello"=="world")
print("hello"!="world")
print("hello">"world") # it is compared lexiographically(dictionary). the word cames first is small and which came latter  is greater.
print("hello">"Hello") # small letters came later so they are grater and capital letter are smaller.
print("____________________")
#* iii.logical operations : python treats "" as true and "hhh" as  false.
print("hello"and"")
print("hello"or"")
print("hello"or"world")  # as the firt val i enough to pecify it true so the ans is first value
print("hello"and"world") # in casse of and last value confirms that it is true  so the answer is true.
print(not "hello")
print(not "")

#* iv.looping
for i in "hello world":
    print(i)

#* v.memberhip operator
val = "hello world"
print("h" in val)
print("hello" not in val)


#! 4.string functions
#* common functions: which are avilable on all itterable
print(len(val))
print(max(val))
print(min(val))
print(sorted(val)) #ascending
print(sorted(val,reverse=True)) #decending
#* string pecific function : only ued in string type
print(val.capitalize()) #make firt alphabate capital
print(val.title()) #make firt alphabate of all capital
print(val.upper()) #make all alphabate  capital
print(val.lower()) #make all alphabate  lower
print(val.swapcase()) #make lower to upper and upper to lower

print(val.count("l")) #count frequency of a substring
print(val.find("l")) #give the first occurence index of a substring. it returns -1 if the substring is not found.
print(val.index("l")) #give the first occurence index of a substring. it give error if the substring is not found.

print(val.startswith('h'))
print(val.endswith('h'))

print("hello, i'm {} i'm {}".format("raja","adult"))
print("hello, i'm {1} i'm {0}".format("raja","adult"))
print("hello, i'm {name} i'm {age}".format(name="raja",age="adult"))

print(val.isalnum()) #check the tring is alpha numeric or not
print(val.isalpha())# is alphabet

print(val.split()) # split a string into a list using whitespace by default
print("-".join(["hello", "world"])) # join list items into a string
print(val.replace("world", "python")) # replace a substring
print("  hello world  ".strip()) # remove leading and trailing whitespace
