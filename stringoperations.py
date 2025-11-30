str1= "computer"
str2="science"

#count the length of string
#print(len(str2))
len1= len(str2)
print(len1)

#for concatenation
final_str=str1+" "+str2 
print(final_str)
print(len(final_str))

#indexing a string

str="sachin raj"
 #str[6] ='b' it is not allowed

ch = str[6]
print(ch)
print(str[5])

#slicing of string

str4= "sachin raj"
print(str4[1:5])
print(str4[:6]) #[0:6]
print(str4[7:]) #[5:len(str)]

#negative indexing

str5="apple"
ch = str5[-3:-1]
print(ch)
