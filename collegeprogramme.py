# # factorial by recursion

# def fact(n):
#      if n==0 or n==1:
#          return 1
#      else:
#          return n*fact(n-1)
# n =int(input("enter the number :"))
# factorial = fact(n)
# print(factorial)

# def swap(x,y):
#   return y,x

# x=2
# y=3
# x,y = swap(x,y)
# print(x)
# print(y)

# def add(a,b):
#     return a+b

# a=5
# b=9
# result =add(a,b)
# print(result)

# a=10
# b=20
# c=81
# if a>b and a>c:
#     print("a is greater")
# elif b>c and b>a:
#     print("b is greater")
# else:
#     print("c is greater")

def check_oddeven(n):
    if n%2==0:
       return "even number"
    else:
        return "odd number"
n=int(input("enter the number: "))
print(check_oddeven(n))