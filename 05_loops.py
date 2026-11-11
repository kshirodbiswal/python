# while loop
num = int(input("Enter a number:"))
i=1
while i<11:
    print(num,'*',i,'=',num*i)
    i+=1


# guessing game
# import random;

# random= random.randint(1,100);
# guess=int(input("Enter a guess between 1 to 100:"))
# counter=0;
# while random!=guess:
#     if guess<random:
#         print('no is small.guess higher')
#     else:
#         print('no is large.guess lower')
#     guess=int(input("Enter a guess:"))
#     counter+=1
    

# print('you guess right in',counter,'attempts.',random,guess)
        

# for loop : in python for loop is operate on either sequence or in range function.
print("for loop using range function:")
for i in range(1,10):
    print(i)

print("for loop using sequence type:")
for i in [10,20,30,40,50]:
    print(i)

#! where to use for loop : when you know the no of itteration performs then we use for loop otherwise we can use while loop. 


# nested loop
# *
# **
# ***
# ****
# *****

rows=int(input("enter a no : "))
for i in range(rows):
    for j in range(i):
        print("*",end=" ")
    print("")

# break : it break out from a loop
for i in range(1,10):
    if i==5:
        break
    print(i)
print("end")

# continue : it skip the single itteration
for i in range(1,10):
    if i==5:
        continue
    print(i)
print("end")

# pass: if you are not sure about what to write in a block of code then we can use pass to ignore the error
for i in range(1,10):
    pass
