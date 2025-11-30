list=[2,1,3]
list.append(4) #adds one element at the end
print(list)
            

#sort
list.sort() # arrange in ascending order
print(list)

# sort
list.sort(reverse=True) #arrange in descending order
print(list)

#apply on strings
list2=["sachin","ayush","ballu","krishna"]
list2.sort()
print(list2)

list3=['a','b','c','d','e']
list3.sort(reverse= True)
print(list3)

#reverse

#list4=['a','b','c','d','e']
list5=[1,2,3,4,5,6]
list5.reverse() #print reverse of the list
print(list5)

list6=[1,2,3,4,5,6]
#list.insert(index,element)
list6.insert(3,10) #insert new element at a given index
print(list6)

list7=[1,2,3,4,5,1,1]
list7.remove(1) #remvoves first occurence of the element
print(list7)


list8=[1,23,45,67,89,99]
list8.pop(5) # remove element at index
print(list8)