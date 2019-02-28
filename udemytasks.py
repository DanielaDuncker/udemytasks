# Section 3


# 8. Strings and Escape Sequences


"""
# 1.
example = "This is an example"

# 2.
example2 = 'This is also an example'

# 3.
example3 = "This has a \"double quote escape sequence\""

# 4.
example4 = "This has a \'single quote escape sequence\'"

print(example, example2, example3, example4)


# -------------------------------------------------


# 1.
lannisters = "JaimeCerseiTyrion"

# 2.
a = lannisters[1]

# 3.
J = lannisters[0]

# 4.
Jaime = lannisters[:5]

# 5.
Cersei = lannisters[5:11]

# 6.
Tyrion = lannisters[11:]

space = ""

print(space)
print(a, J, Jaime, Cersei, Tyrion)
"""


# 10. String Methods


"""
# 1.
py = "Python"

# 2.
pyLen = len(py)

# 3.
sliceLen = len(py[1:4])

# 4.
num = 1.32

# 5.
stringed = str(num)[3]


print(py, pyLen, sliceLen, num, stringed)

# --------------------------------------------------------

# 1.
upCase = "upper"

print(upCase.upper())

# 2.
lowCase = "LOWER"

print(lowCase.lower())
"""


# 12. Print


"""
# 1.
hiWorld = "hello" + "world"

# 2.
num1 = 11

# 3.
num2 = 38

# 4.
together = str(num1) + str(num2)

print(hiWorld)
print(together)

# ------------------------------------------------------

# 1.
restaurant = input("Your favorite restaurant")

# 2.
visit = input("The place you want to visit")

# 3.
nickName = input("Your nickname or if you don't have a nickname then your first name")

# 4.
output = "Your favorite restaurant is%s, you want to visit%s, and your nickname or first name is%s." %(restaurant, visit, nickName)

print(output)
"""


# Section 4


# 14. Flow Control and Comparators


"""
# 1.
math = 4 > 3

# 2.
math2 = 3 > 4

# 3.
math3 = 4 >= 4

# 4.
math4 = 4 >= 5

# 5.
math5 = 7 < 8

# 6.
math6 = 8 < 7

# 7.
math7 = 6 <= 6

# 8.
math8 = 3 <= 2

# 9.
math9 = 4 == 4

# 10.
math10 = 5 == 3

# 11.
math11 = 5 != 4

# 12.
math12 = 2 != 2
"""


# 16. Boolean Operators


"""
# 1.
andTrue = True and True

# 2.
andFalse = True and False

# 3.
orTrue = True or False

# 4.
orFalsies = False or False

# 5.
notTrue = not False

# 6.
notFalse = not True

# -----------------------------------------------------

# 1.
var1 = not 3 > 1 and 5 != 2 and 6 == 6

print(var1)

# 2.
var2 = 4 * 2 != 6 and 7 % 6 == 1

print(var2)
"""


# 18. If, Else, and Elif


"""
# 1.
name = input("Enter your name")

nameLen = len(name)

if nameLen < 4:
    print("Your name is less than 4 characters")
elif nameLen < 10:
    print("Your name is at least 4 characters and less than 10 characters")
else:
    print("Your name is very long")


# Katso vendingMachine.py
"""


# 20. Functions


"""
# 1.
def ex():
    print("This is a function")

# 2.
five = 5

# 3.
def single(a):
    print(a)

# 4.
ex()

# 5.
single(five)

# -------------------------------------------------------

# 1.
int1, int2, int3 = 3, 4, 5

# 2.
def diff(a, c):
    print(c - a)

# 3.
def mult(a, b, c):
    print(a + b * c)

# 4.
diff(int1, int3)

# 5.
mult(int1, int2, int3)

# -----------------------------------------------------

# 1.
flo1, flo2, flo3 = 1.5, 2.5, 3.5

# 2.
def div(a, b):
    return a / b

# 3.
def div2(c, d, e):
    return div(c, d) / e

# 4.
step2Func = div(flo1, flo2)

# 5.
print(step2Func)

# 6.
print(flo1, flo2, flo3)
"""


# 23. Importing Modules



# 1.
import random

# 2.
from math import *

# 3.
from sys import exit

# 4.
rand = random.random() * 100

# 5.
square = sqrt(rand)

# 6.
exit(square)





