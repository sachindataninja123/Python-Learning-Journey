#print(range(5))
'''seq = range(10)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])
print(seq[5])'''

# by loop
#seq=range(5)
#for i in range(5) :
 #   print(i)

 # syntax of range (start? , stop , step?) where start and stop is optional

'''for ele in range(2,10) : #range(start,stop)
    print(ele)

for val in range(2,20,2) : # range(start,stop, step)
    print(val)'''

# to print even number by range 
 
#for ele in range(2,201,2) :
    #print(ele)

# to print odd number by range 
#for ele in range(1,201,2) :
   # print(ele)



# QUESTIONS
# 1. to print numbers 1 to 100

#for val in range(1,101):
    #print(val)

# 1. to print numbers 100 to 1
#for ele in range(100,0,-1):
   # print(ele)


# to print a multiplication of nuumber n
n =int(input("enter the value of n: "))
for table in range(1,11) :
   print(n*table)


'''pass statement (that are used to leave emptyblock of code)'''

for ele in range(10) :
   pass

print("hello world")