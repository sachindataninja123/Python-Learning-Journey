# armstrong number

# num=int(input("enter a number :"))
# sum = 0
# temp = num
# while temp>0:
#     digit = temp%10
#     sum +=digit ** 3
#     temp //=10
# if num == sum :
#     print(num,"is an armstrong number")
# else:
#     print(num,"is not an armstrong number")


# PRIME NUMBER CHECK
# num=int(input("enter a number:"))
# if num > 1:
#     for i in range(2,num):
#         if num % i == 0:
#             print("not prime number")
#             break
#     else:
#             print("prime")
# else:
#     print("not prime")

# FIBONACCI SEQUENCE
# limit =int(input("Enter a limit: "))
# a = 0
# b = 1
# while a <= limit:
#     print(a,end=" ")
#     a,b = b, a+b

# FACTORIAL OF A NUMBER
# num = int(input("Enter a Number :"))
# fact = 1
# for i in range(1, num+1):
#     fact = fact*i
# print("factorial :", fact)

# FACTORIAL BY RECURSION
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*fact(n-1)

# print(fact(5))

# leap year or not
# year = int(input("enter the year:"))
# if(year % 400 == 0):
#     print("Leap year")
# elif(year % 100 == 0):
#     print("not a leap year")
# elif(year % 4 == 0):
#     print("leap year")
# else:
#     print("not a leap year")

# Greatest of three numbers
# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))
# c = int(input("Enter a number:"))
# if(a>b and a>c):
#     print("A is greatest number")
# elif(b>c and b>a):
#     print("b is greatest")
# else:
#     print("c is greatest number")

# ARMSTRONG number
num = int(input("enter a number:"))
sum = 0
temp = num
while temp > 0:
    digit  = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print("armstrong number")
else:
    print("not an armstrong number")

