#CONDITIONAL STATEMENT

'''age= int(input("enter the age of the persons:"))

if(age >= 18) :
    print("person is eligible for vote")
else :
    print("person is not eligible for vote")

#just for traffic light

light=input("enter the light : ")  
if(light =="red") :
    print("stop")
elif(light =="green") :
    print("go")
elif(light =="yellow") :
    print("stop and look")
else :
    print("can't any action") '''

#GRADE STUDENTS BASED ON MARKS

'''math =int(input("enter the marks of maths: "))
gk = int(input("enter the marks of gk : "))
comp = int(input("enter the marks of comp : " ))
etc = int(input("enter the marks of etc : "))
science = int(input("enter the marks of science : "))

total_marks= math+gk+comp+etc+science
percentage = total_marks*100/500
print("the percentage is : " ,percentage)

if(percentage  >= 90) :
    print("A")
elif(percentage >=80 and percentage < 90) :
    print("B")
elif(percentage >= 70 and percentage <80) :
    print("C")
elif(percentage >=40 and percentage <70 ) :
    print("D")
else :
    print("fail")'''


# NESTING

age=int(input("enter the age of the person:"))

if(age >= 18):
    if(age >= 80):
       print("cannot drive")
    else :
        print("can drive")
else:
    print("cannot drive")