#recursive function

'''def show(n):
    if(n==0): # base case
        return
    print(n)
    show(n-1)

show(5)

def cal_fact(n):
    if(n==0 or n==1):
        return 1
    else:
     return n* cal_fact(n-1)


n =int(input("enter the number: "))
print(cal_fact(n))'''

# WARF TO CALCULATE THE SUM OF FIRST N NATURAL NUMBERS
 
def cal_sum(n):
   if(n==0):
      return 0
   else:
      return cal_sum(n-1) + n

a =int(input("enter the number : "))
sum =cal_sum(a)
print("sum is : ",sum)

#WARF to print all the elements in a list
#hint : use list& index as a 

def print_list(list, idx=0):
   if(idx == len(list)) :
      return
   print(list[idx])
   print_list(list,idx+1)

bikes =["ninja","pulsar","apache","bullet","glamour","tvs"]
print_list(bikes)
