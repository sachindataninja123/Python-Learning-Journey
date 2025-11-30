# num = int(input("Enter the number:")) 
# fact = 1
# for i in range(1, num+1):
#     fact *= i
# print("factorial:", fact)

def fact(n):
     if n == 0 or n==1:
        return 1
     else:
        return n*fact(n-1)
    
print(fact(1))