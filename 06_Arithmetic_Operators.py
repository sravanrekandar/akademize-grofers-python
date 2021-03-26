"""Arithmetic Operators.
Action	                        Common Symbol
---------------------------------------------
Addition	                        +
Subtraction	                        -
Multiplication	                    *
Division	                        /
Modulus (associated with integers)	%
"""

a = 15
b = 2

print(str(a) + " + " + str(b) + " = " + str(a+b))
# 15 + 2 = 17

print(f"{a} - {b} = {a-b}")
# 15 - 2 = 13

print("{} * {} = {}".format(a, b, a*b))
# 15 * 2 = 30

print("{x} / {y} = {div}".format(y=b, x=a, div=a/b))
# 15 * 2 = 7.5

print(f"{a} // {b} = {a//b}")
# 15 // 2 = 7

print(f"{a} % {b} = {a%b}")
# 15 % 2 = 1