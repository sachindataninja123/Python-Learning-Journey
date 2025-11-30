#mydict.keys() # returns all keys
employee ={
    "name" :"mahesh",
    "id no" :10023,
    "blood group" : " b positive",
    "designation" : "worker",
    "salary" : 40000
}
'''print(employee.keys())
print(len(employee.keys()))
print(list(employee.keys())) # type casting in list
print(len(list(employee.keys())))'''

# mydict.values() returns all value
print(employee.values())

# mydict.items() returns all (key ,val) pairs as tuple
print(employee.items())

#mydict.get("key") # returns the key according to value
print(employee.get("name"))
#print(employee.get("name2")) #it returns none if it is not exist in code
#print(employee["name3"]) # it directly returns error if the code is not exist

#mydict.update(newdict) # inserts the specified items to the dictionary
employee.update({"father's name" : "mahesh bhatt"})
print(employee)


