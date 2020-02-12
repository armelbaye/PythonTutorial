"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
""" 

#to get a data type of a variable
x = range(6)
print(x)
print(type(x))

z = 20
print(z)
print(type(z))

p = 20.8
print(p)
print(type(p))

t = "hello"
print(t)
print(type(t))

b = 1j
print(b)
print(type(b))

c = ["apple", "banana", "orange"]
print(c)
print(type(c))

v = ("java", "c++", "python")
print(v)
print(type(v))

l = {"name": "john", "age" : '36'}
print(l)
print(type(l))

var_7 = {"apple", "banana", "cherry"}
print(var_7)
print(type(var_7))

Var_8 = frozenset({"apple", "banana", "cherry"})
print(Var_8)
print(type(Var_8))

VAR9 = True
print(VAR9)
print(type(VAR9))

VAR_10 = b"Hello"
print(VAR_10)
print(type(VAR_10))

_VaR = bytearray(5)
print(_VaR)
print(type(_VaR))

var11 = memoryview(bytes(5))
print(var11)
print(type(var11))