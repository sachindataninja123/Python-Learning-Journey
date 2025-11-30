'''a= 10
b=9
c= a+b  # normal sum program

print(c)'''
#function defination
'''def cal_sum(a,b) : # where (a,b) is parameter
    sum = a+b 
    print(sum)
    return sum

cal_sum(20,90) # and(20,90) is argument
cal_sum(65,89) #function call
cal_sum(89,56)
cal_sum(4,8)'''


'''def print_gm():
    print("good morning")

print_gm()
print_gm()'''

# average of 3 numbers
'''def avg(a, b, c) :
    return (a + b + c) / 3

    
cal_avg= avg(5,5,5)
print("average :",cal_avg)'''

def sum(a,b):
    c= a+b
    return c

print(sum(5,6))

def cal_avg(a,b,c) :
    avg = (a+b+c)/ 3
    return avg

avg=cal_avg(8,5,5)
print("average is:",avg)


#default parameters
def cal_multi(a=1,b=2): #(a,b=1)
    return a*b

multi =cal_multi(8)
print(multi)