

# Operators are used to perform operations on variables and values.

# 1. Arithmetic operators
a, b = 10, 3
print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.333...
print(a // b)  # Floor division: 3
print(a % b)   # Modulus: 1
print(a ** b)  # Exponentiation: 1000

# 2. Comparison operators
print(a == b)  # Equal to: False
print(a != b)  # Not equal to: True
print(a > b)   # Greater than: True
print(a < b)   # Less than: False
print(a >= b)  # Greater than or equal to: True
print(a <= b)  # Less than or equal to: False

# 3. Logical operators
x, y = True, False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# 4. Bitwise operators
p, q = 6, 3  # Binary: 110 and 011
print(p & q)   # AND: 2
print(p | q)   # OR: 7
print(p ^ q)   # XOR: 5
print(~p)      # NOT: -7
print(p << 1)  # Left shift: 12
print(p >> 1)  # Right shift: 3

# 5. Assignment operators
number = 10
number += 2   # Same as: number = number + 2
number -= 1
number *= 3
number /= 11
print(number)  # 3.0
# a++ and ++a is not allowed in python

# 6. Identity operators : it returns true if both values are in same memory location
first = [1, 2]
second = first
third = [1, 2]
print(first is second)      # True (same object)
print(first is not third)   # True (different objects)

# 7. Membership operators
fruits = ["apple", "banana"]
print("apple" in fruits)       # True
print("mango" not in fruits)   # True