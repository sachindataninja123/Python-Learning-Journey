# while loop
#i=1
#while i<=10 :
   # print("i love india")
   # i += 1

'''x= 1
while x<=50 :
    print(x)
    x += 1'''

'''# in reverse 
i=5
while i>=1 :
    #print(i)
    i -= 1

    #y =6
    #while y < 7: # don't create infinite loop
       # print(i)
       # i -= 1

#practice questions

# 1 print numbers from 1 to 100
i =1 
while i <= 100 :
    #print(i)
    i += 1

    
# 2 print numbers from 1 to 100
y =100 
while y >=1 :
   # print(y)
    y -= 1

# 3 print the multiplication table of a number n
#n = int(input("enter the value of n : "))
i =1
while(i<=10) :
    #print(n*i)
    i += 1


# print the elements of the following list using a loop
#[1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]
idx=0
while idx <len(nums) :
    #print(nums[idx])
    idx += 1

cars =["BMW","AUDI","FERRARI","MERCEDES","LAMBHORGINI"]
index=0
while(index < len(cars)) :
    #print(cars[index])
    index += 1
'''

# 5 . search the number x in this tuple using loop:
#[1,4,9,16,25,36,49,64,81,100]
num = (1,4,9,16,25,36,49,64,81,100)
#print(type(num))

'''x= int(input("enter the vlaie of x : "))
i=0
while i< len(num) :
    if(num[i] == x):
     # print("x is found at index",i)
      break #if we not use it then it prints after check the value of x
    else :
       # print("finding...")
    i += 1
    '''
'''y = int(input("enter the value of y: "))

w =0
while w <= 6 :
    if( w == y):
        print(w)
        break
    else:
        print("not found")
    w += 1'''


'''b= int(input("enter the value of b: "))
z=0
while z <= 10 :
    if(z == b):
        z += 1
        continue # used to skip something in iteration
    print(z)
    z +=1'''


'''j = 1
while j <= 10:
    if(j % 2 == 0) :
     j +=1
    continue
print(j)
j += 1'''

i =1
while i<= 10 :
    if(i % 2 != 0):
        i +=1
        continue
    print(i)
    i += 1