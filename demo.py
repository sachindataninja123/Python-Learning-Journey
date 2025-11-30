#print("hello world")

#print(55+10)
#print("hii how are you")
# #leap year by function

def a(year): 
    if year%400 == 0:
        print("leap year")
    elif year%100 == 0:
        print(" not a leap year")
    elif year% 4== 0:
        print("leap year")
    else :
        print("not a leap year")

        #year = 3000
        year = int(input("enter the year:"))
        a()
        