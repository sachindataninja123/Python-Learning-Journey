#for loop 
#list
'''nums =[1,2,3,4,5]

for val in nums :
    print(val)

#tuple
fruits = ("apple","mango","strawberry","blackberry","pineapple")

for val in fruits :
    print(val)

#string
str = "hello world"
for char in str :
    print(char)


#sets
set ={5.4,3.6,4.6,9.0,7.8}  

for val in set :
    print(val)


#dictionary
my_dict = {
    "name"  :"sachin",
    "class" : "b.tech",
    "cgpa"  :9.8,
    "marks" : [89,90,98],
}

for key in my_dict :
    print(key, ":",my_dict[key])

str = "apna college"
for char in str :
    if (char == 'l') :
        print(" l is found")
        break

    print(char)
else :
    print("end")'''



    # QUESTIONS

#1. PRINT THE ELEMENTS OF THE FOLLOWING LIST USING A LOOP :
    #[1,4,9,16,25,36,49,64,81,100]

#num =[1,4,9,16,25,36,49,64,81,100] 
#for val in num:
 #       print(val)
    

# search for a number x in this tuple using loop:
#(1,4,9,16,25,36,49,64,81,100)

'''value =(1,4,9,16,25,36,49,64,81,100,64)
x= int(input("enter the value of x: "))


idx = 0
for ele in value :
        if(ele == x) : # to finding that value of x like it it is called linear search
          print("element is found at idx",idx)
          break #if it is not use then print both index value of x
        idx += 1'''


# Q. WAP TO FIND THE SUM OF FIRST N NATURAL NUMBERS.(USING WHILE)

#n = int(input("enter the natural number : "))
'''sum =0
i = 1
while( i <= n) :
      sum += i
      i += 1

print("total sum is :",sum)'''

# by for loop
'''n = int(input("enter the natural number : "))
sum =0
for val in range(1,n+1) :
      sum += val

print("total sum",sum)'''


# wap to find the factorial of first n numbers.(using for)
# by while loop
'''n = int(input("enter the natural number : "))
fact = 1
i =1
while i <= n:
      fact *= i
      i +=1

print("factorial is  =", fact)'''

#by for loop
n = int(input("enter the natural number : "))
fact =1

for i in range(1,n+1):
      fact *= i 

print("factorial is :",fact)
      
      