"""
variable do not need to be declared with  
any particular type. they can change type after
being set. below x is an int and then can be
changed to a string.

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)

"""
x = 5
x = "5 is a not a prime number"
y = 'single quoted string'
print(x)
print(y)

#you can assign values to multiple variables.
a,b,c = 'armel', 'brandon', 'mike'
print(a)
print(b)
print(c)

#And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

#To combine both text and a variable, Python uses the + character:
x = "awesome"
print("Python is " + x)

#You can also use the + character to add a variable to another variable:
x = "Python is "
y = "awesome"
z =  x + y
print(z)

#For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

#cannot concatenate strings and primitives.

#Global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#If you create a variable with the same name inside a function, 
# this variable will be local, and can only be used inside the function. 
# The global variable with the same name will remain as it was, global and with the original value.
p = "great"

def func():
  p = "fantastic"
  print("Python is " + p)

func()

print("Python is " + p)

#To create a global variable inside a function, you can use the global keyword.
def afunc():
  global z
  z = "amazing"

afunc()

print("Python is " + z)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

n = "thrilling"

def nfunc():
  global n
  n = "perfect"

nfunc()

print("Python is " + n)

