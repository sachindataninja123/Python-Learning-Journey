info={
    "key" : "value",
    "name" : "sachin",
    "subjects" :["python","c","java","php"], #in dictionary we create lists and tuple
    "topics" : ("dictionry","sets"),
    "cgpa" :8.0,
    "marks" :89,
    "age" : 23,
    "is adult" :True,
    "class" :"b.tech"

}
print(info)
print(type(info))

#accesible dictionary like this
print(info["name"])
print(info["cgpa"])
print(info["class"])
print(info["is adult"])

#dictionary is mutuble 
info["name"] ="rajesh"
info["topics"] =("only loops","function","recursion")
info["surname"] ="kushwaha" #add something in dictionary
print(info)

#null dictionary
null_dict={}
null_dict["name"]="sachin"
print(null_dict)


# NESTED DICTIONARY
student = {
    "name":"sachin",
    "class" :"b.tech",
    "roll no" :"24cs08",
    "subjects" : {
       "phy" :89,
       "chem" :80,
       "math" :96,
       "etc" :45,
    }
    
}
print(student["subjects"])
print(student["subjects"]["math"])
