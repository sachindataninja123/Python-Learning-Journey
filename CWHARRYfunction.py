#GEOMETRIC MEAN  a*b/a+b

a= 4
b=5
gmean = (a*b)/(a+b)
print(gmean)
# by function
def cal_gmean(a,b):
    gmean=(a*b)/(a+b)
    print("GEOMETRIC MEAN IS ",gmean)

def isgreater(a,b) :
 if(a >= b):
   print("A is greater ")
 else :
   print("B IS GREATER")
def islesser(a,b) :
  if(a <= b):
   print("A is lesser ")
  else :
   print("b is lesser")
  
a=int(input("enter the value of a : "))
b = int(input("enter the value of b : "))
#if(a >= b):
 #   print("A is greater ")
#else :
 #   print("B IS GREATER")
isgreater(a,b)
islesser(a,b)
cal_gmean(a,b)

c=int(input("enter the value of c : "))
d = int(input("enter the value of d : "))
#if(c >= d):
 #   print("c is greater ")
#else :
#print("d IS GREATER")
isgreater(c,d)
islesser(c,d)
cal_gmean(c,d)