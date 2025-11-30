#1 WAP TO ASK THE USER TO ENTER OF THEIR 3 MOVIES AND STORE THEM IN A LIST

'''movies=[]

movie1=input("enter the movie 1 name : ")
movie2=input("enter the movie 2 name : ")
movie3=input("enter the movie 3 name : ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)'''

#2 WAP TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS.(HINT:USE COPY()METHOD)
 
list =['m','a','a','m']
copy_list = list.copy()
copy_list.reverse()

if(copy_list == list) :
    print("palindrome")
else:
    print("not palindrome")

#WAP TO COUNT THE NUMBER OF STUDENTS WITH THE "A" GRADE  IN THE FOLLOWING TUPLE
grade=("c","d","a","a","b","b","a")
print(grade.count("a"))

#STORE THE ABOVE VALUES IN A LIST AND SORT THEM FROM "A" TO "D"
grade2 =["A","B","A","C","A","B","D"]
grade2.sort()
print(grade2)