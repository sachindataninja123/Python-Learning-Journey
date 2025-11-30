#1
'''store following word meanings in a python dictionary:
table :"a piece of furniture","list of facts and figures"
cat : "a small animal" '''

dictionary={
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts and figures"]
    
}
print(dictionary)


#2 question
subjects ={

    "python","java","c++","c","python","javascript","java",
    "python","java","c++"
}
print(subjects)
print(len(subjects))

'''3. WAP to enter marks of 3 subjects from the user and store them in a dictionary
start with an empty dictionary & add one by one. use subject name as key and marks as value'''

'''marks={}

x=int(input("enter the phy marks  : "))
marks.update({"phy" : x})

y = int(input("enter the marks of math : "))
marks.update({"math" : y})

z = int(input("enter the marks of comp : "))
marks.update({"comp" : z})

print(marks)'''

# 4 figure out a way to store 9 and 9.0 as seprate values in the set.
#(you can take help of built - in data types)

#values={9,9.0} #python takes 9 or 9.0 as a same value so we print it other method
#values={9,"9.0"}
#print(values)

#to print it by second method
values = {
    ("float",9.0),
    ("int", 9)
}
print(values)