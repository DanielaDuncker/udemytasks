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

print(example)
print(example2)
print(example3)
print(example4)


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


# Section 5


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


# 22. Importing Modules


"""
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
"""


# 24. Built-In Functions


"""
# 1.
print(abs(2))

# 2.
print(abs(-2))

# 3.
print(type(1.2))

# 4.
print(type(3))

# 5.
print(type(True))

# 6.
print(type("hello"))

# ------------------------------------------------------------------------

# 1.
print(max(2, 7, 630, 28, 62))

# 2.
print(max("elsa", "alsa", "ilsa", "ulsa", "ylsa"))

# 3.
print(min(2, 7, 630, 28, 62))

# 4.
print(min("elsa", "alsa", "ilsa", "ulsa", "ylsa"))
"""


# Section 6


# 26. Lists


"""
# 1.
listStr = ["a", "b", "c", "d"]

# 2.
listNum = [1, 2, 3]

# 3.
listMix = ["hi", 4, "you", "are", True]

# 4.
print(listStr)

# 5.
print(listNum[1])

# 6.
print(listMix[4])

# -------------------------------------------------------------------

# 1.
reAssign = [1, 2, 3]

print(reAssign)

# 2.
reAssign[0] = 2

# 3.
reAssign[1] = 3

# 4.
reAssign[2] = 4

# 5.
reAssign.append(6)

# 6.
print(reAssign)

# -------------------------------------------------------------------

# 1.
listSli = [1, 2, 3, 4, 5, 6, 7]

# 2.
print(listSli[:4])

# 3.
print(listSli[2:5])

# 4.
print(listSli[1:])

# -------------------------------------------------------------------

# 1.
Strlist = ["Bob Dylan", "Like a", "Rolling Stone"]

# 2.
print(Strlist.index("Rolling Stone"))

# 3.
Strlist.insert(0, str(1965))

# 4.
print(Strlist)

# -------------------------------------------------------------------

# 1.
surName = ["McCartney", "Lennon", "Starr", "Harrison", "Sutcliffe"]

# 2.
surName.remove("Sutcliffe")

# 3.
print(surName)

# 4.
print(surName.pop(1))

# 5.
print(surName.pop())

# 6.
print(surName)
"""


# 28. For Loops and Tuples


"""
# 1.
tupVal = (2.5, 3, True, "hello")

# 2.
print(tupVal)

# 3.
print(tupVal[1])

# 4.
print(tupVal[0])

# 5.
print(tupVal[:3])

# 6.
print(tupVal[1:])

# 7.
print(tupVal[1:3])

# ----------------------------------------------------------------

# 1.
tupLoop = ("Bohr", "Leibniz", "Einstein")

# 2.
emptyLoop = []

# 3.
listLoop = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 4.
for names in tupLoop:
    print(names)

# 5.
for num in listLoop:
    if num > 1 and num < 8:
        emptyLoop.append(num)

# 6.
print(emptyLoop)
"""


# 30. Dictionaries


"""
# 1.
dictionary1 = {"a": "1", "b": "2", "c": "3"}

# 2.
print(dictionary1["a"])

# 3.
dictionary1["d"] = 4

# 4.
print(dictionary1)

# 5.
print(len(dictionary1))

# --------------------------------------------------------------

# 1.
dictionary2 ={1: "Gwen", 2: "Arthur"}

# 2.
print(dictionary2)

# 3.
dictionary2[1] = "Merlin"

# 4.
print(dictionary2)

# 5.
del dictionary2[2]

# 6.
print(dictionary2)
"""


# 32. Using Functions With List


"""
# 0.
intsList = [1, 2, 3, 4, 5,]
strList = ["a", "b", "c", "d", "e"]
floList = [1.1, 1.2, 1.3, 1.4, 1.5]

# 1.
def passer(aList):
    return aList

print(passer(intsList))
print(passer(strList))
print(passer(floList))

# 2.
def access(theList):
    return theList

print(access(intsList))
print(access(strList))
print(access(floList))

# 3.
def product(a):
    print(a[0] * a[3])

product(intsList)

def concatenator(b):
    holder = ""
    for x in b:
        holder += x
    print(holder)

concatenator(strList)

def quotiet(c):
    print(c[2] / c[1])

quotiet(floList)

# 4.

def three(d):
    d.append(6)
    d.insert(0, 1)
    d.remove(1)
    print(d)

three(intsList)
"""


# 34. Using An Entire List Within A Function


"""
# 0.
inputList = [5, 4, 3, 2, 1]

# 1.
def one_input(a_list):
    for item in a_list:
        print(item)

one_input(inputList)

# 2.
range1 = range(10)
range2 = range(4, 8)
range3 = range(5, 21, 5)

# 3.
def range_return(the_return):
    return the_return

print(range_return(range1))

# 4.
def range_iterator(a_range):
    for element in range(0, len(a_range)):
        print(a_range[element])

range_iterator(range2)

# 5.
def range_modifier(modified):
    for items in range(0, len(modified)):
        modified[items] += 3
    print(modified)

range_modifier(inputList)

# 6.
def two_inputs(list1, list2):
    print(list1, list2)

two_inputs(inputList, range3)

# 7.
all_strings = [["apple", "pear"], ["broccoli", "carrots", "corn"], ["pork", "beef"]]

def concatenator(list_of_strings):
    new_list = []
    for index in range(0, len(list_of_strings)):
        for strings in list_of_strings[index]:
            new_list.append(strings)
        print(new_list)

concatenator(all_strings)
"""


# 36. While Loops


"""
# 1.
a_counter = 0

while a_counter < 5:
    print("a string")
    a_counter += 1

b_counter = 1
emp_list = []

while b_counter < 4:
    emp_list.append(b_counter)
    b_counter += 1

print(emp_list)

# 2.
break_counter = 0
while True:
    print("a string")
    break_counter += 1
    if break_counter > 5:
        break

fruit = input("What is my favourite fruit? ")

while fruit != "Apple":
    print(fruit + " is not my favourite fruit!")
    fruit = input("What is my favourite fruit? ")
else:
    print("That is correct, " + fruit + " is my favourite fruit!")
"""


# 38. More For Loops


# 1.
str1 = "Borneo"

for char in str1:
    print(char)

for char in range(len(str1)):
    print(str1[char])

# 2.
intList = [0, 4, 8, 90]

for ints in intList:
    print(ints, end="X")

# 3.
dictionary = {"Mercury": 1, "Earth": 3, "Mars": 4}

for key in dictionary:
    print(str(dictionary[key]) + " " + key)

# 4.
list1 = [10, 488, 2.1, 29]
list2 = [32, 30, 1, 0]

emp = []
for num1, num2 in zip(list1, list2):
    emp.append(num1 + num2)

print(emp)

# 5.
tup = ("scorpio", "aquarius", "pisces", "libra", "sagittarius")

for index in range(len(tup) - 1):
    print(tup[index])
else:
    print(tup[4])

for index in range(len(tup)):
    if index < 3:
        print(tup[index])

    else:
        break
else:
    print("This should not be printed")





















