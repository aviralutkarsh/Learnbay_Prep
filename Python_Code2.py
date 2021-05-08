a=47
b=47
print(id(a))
print(id(b))
# The ID for both the variables declared above is same because for int type variable, 
# for values between -5 to 256, memory address is shared.

c=697
d=697
print(id(c))
print(id(d))
# The ID for both the variables declared above is different because their values even though same, lie outside 
# the range of -5 to 256. Hence, here the memory address is not shared.

a=7
b=2
print(str(a+b))
print(str(a-b))
print(str(a*b))
print(str(a/b))
print(str(a%b)) # Modulo operator used for getting the remainder
print(str(a//b)) # FLoor operator used for getting quotient
print(str(a**b)) #Exponent Operator

#Boolean Opearators
a=47
b=-23
print(str(a>b))
print(str(a<b))
print(str(a>=b))
print(str(a<=b))

print (10 and 20)
print (0 and 20)
print (20 and 0)
print (0 and 0)
print (10 or 20)
print (0 or 20)
print (20 or 0)
print (0 or 0)
print (not 10)
print (not 0)

# print ( 10 and 20 ) -> 10 and 20 are non zero numbers and are "true". If the first operand of “and” expression
# is false, return the first operand. Otherwise, evaluate and return the second operand. So 20 is printed.

# print ( 0 and 20 ) -> O is "false" in Python. If the first operand of an “and” expression is false, return the 
# first operand. Otherwise, evaluate and return the second operand. So 0 is printed.

# print ( 20 and 0 ) -> If the first operand of “and” expression is false, return the first operand. 
# Otherwise, evaluate and return the second operand. So 0 is printed.

# print ( 0 and 0 ) -> If the first operand of “and” expression is false, return the first operand. 
# Otherwise, evaluate and return the second operand. So 0 is printed.

# print ( 10 or 20 ) -> If the first operand of an “or” expression is true, return the 
# first operand. Otherwise, evaluate and return the second operand. So 10 is printed.

# print ( 0 or 20 ) -> If the first operand of an “or” expression is true, return the 
# first operand. Otherwise, evaluate and return the second operand. So 20 is printed.

# print ( 20 or 0 ) -> If the first operand of an “or” expression is true, return the 
# first operand. Otherwise, evaluate and return the second operand. So 20 is printed.

# print ( 0 or 0 ) -> If the first operand of an “or” expression is true, return the 
# first operand. Otherwise, evaluate and return the second operand. So 0 is printed.

# print ( not 10 ) -> 10 as a non zero number is "true". so "not true" is "false". Hence, "False" is printed.

# print ( not 0 ) -> 0 is "false" in python. so "not false" is "true". Hence, "True" is printed.


print(bin(10))
print(bin(20))
print(0b00000)
print(0b11110)
print(10 & 20)
print(10 | 20)
print(10 ^ 20)
print(~ 10)
print(10 << 2)
print(10 >> 2)

# & Truth Table
# 1 & 1 = 1
# 1 & 0 = 0
# 0 & 1 = 0
# 0 & 0 = 0

# | Truth Table
# 1 | 1 = 1
# 1 | 0 = 1
# 0 | 1 = 1
# 0 | 0 = 0

# ^ Truth Table
# 1 ^ 1 = 0
# 1 ^ 0 = 1
# 0 ^ 1 = 1
# 0 ^ 0 = 0

# ~(num) = -(num+1)
# << - left shift   -> Num << no of bits  ->  num << x == num * (2**x)
# >> - right shift  -> Num >> no of bits  ->  num >> x == num // (2**x)


# print(10 & 20) -> 01010 & 10100 -> 00000 -> 0
# print(10 | 20) -> 01010 | 10100 -> 11110 -> 30
# print(10 ^ 20) -> 01010 ^ 10100 -> 11110 -> 30
# print(~ 10) -> -(10+1) -> -11
# print(10 << 2) -> 10 * (2**2) -> 40
# print(10 >> 2) -> 10 // (2**2) -> 2


a = 10
b = 10
print(str(a))
print(str(b))
print(id(a))
print(id(b))
# The value of a and b is 10 which lies in the range [-5,256], so they have the same memory address.
print(a is b) # This will give "True"
print(a is not b) # This will give "False"

a = 1000
b = 1000
print(str(a))
print(str(b))
print(id(a))
print(id(b))
# The value of a and b is 1000 and doesn't lie in the range [-5,256], so they don't share the same memory address.
print(a is b) # This will give "False"
print(a is not b) # This will give "True"


print(29 << 2)
print ( 10 +( 10 * 32 )// 2 ** 5 & 20 +(~( -10 ))<< 2 )
print (20 & 116)

# print ( 10 +( 10 * 32 )// 2 ** 5 & 20 +(~( -10 ))<< 2 )
# 10 +( 10 * 32 )// 2 ** 5 & 20 +(~( -10 ))<< 2
# 10 + 320 // 2 ** 5 & 20 + 9 << 2
# 10 + 320 // 32 & 20 +9 << 2
# 10 + 10 & 20 + 9 << 2
# 20 & 29 << 2
# 20 & 116
# 20


print ( '2' in 'Python2.7.8' )
print ( 10 in [ 10 , 10.20 , 10 + 20j , 'Python' ])
print ( 10 in ( 10 , 10.20 , 10 + 20j , 'Python' ))
print ( 2 in { 1 , 2 , 3 })
print ( 3 in { 1 : 100 , 2 : 200 , 3 : 300 })
print ( 10 in range ( 20 ))



# Converting an integer value into other number systems:
a= 9876
b= bin(a)
c= oct(a)
d= hex(a)
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print("The value of the integer " + str(a) + " in other number systems is:")
print("It is", b , "in the binary system.")
print("It is", c , "in the octal system.")
print("It is", d , "in the hexadecimal system.")



a = 0b1010000
print (a)
b = 0o7436
print (b)
c = 0xfade
print (c)
print (bin(80))
print (oct(3870))
print (hex(64222))
print (bin(a))
print (bin(c))
print (oct(c))
print (oct(b))
print (hex(a))
print (hex(c))
