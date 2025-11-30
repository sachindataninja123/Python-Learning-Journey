# WAF TO PRINT THE LENGTH OF A LIST.(list is the parameter)

'''cars=["swift","grand vitara","fortuner","lambo","ferrari"]
bikes =["ninja","yamaha","suzuki","bullet","g.t","apache"]

#print(type(cars))

def print_len(list):
    print(len(list))

print_len(cars)
print_len(bikes)'''

#WAF TO PRINT THE ELEMENTS OF A LIST IN A SINGLE LINE.(LIST IN THE PARAMETER)
'''cars=["swift","grand vitara","fortuner","lambo","ferrari"]
#bikes =["ninja","yamaha","suzuki","bullet","g.t","apache"]

def print_ele(list) :
    for items in list :
        print(items, end=" ")
    
print_ele(cars)
#print_ele(bikes)'''


# WAF to find the factorail of n.(n is the parameter)

'''def cal_fact(n) :
    fact =1
    for i in range(1,n+1) :
        fact *= i
    print(fact)
 
b = int(input("enter the number : "))
cal_fact(b)


# WAF TO CONVERT USD TO INR

def converter(usd_val):
    inr_val = usd_val*83
    print(usd_val, "USD =",inr_val ,"INR")

a = int(input("enter the usd :"))
converter(a)'''

#WAF TO CHECK GIVEN NUMBER IS ODD OR EVEN

def cal_num(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")

n= int(input("enter the number :"))
cal_num(n)

