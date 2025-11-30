# set methods
collection =set() # empty set 

# 1. set.add() add something in set
collection.add(1)
collection.add(2)
collection.add(1)
collection.add("sachin")
collection.add(8.8)
print(collection)
print(len(collection))

# 2. set.remove() remove something from set
#collection.remove("sachin")
#print(collection)

#3. set.clear() # empties the set
#collection.clear()
#print(len(collection))

#4. set.pop() # removes a random value from set
collection.pop()
print(collection)
print(len(collection))

collection2 ={"hello","sachin","world","python"}
print(collection2.pop())


#5. setunion(set2) # combines both set value and return new
set1= {1,2,3,4,5}
set2={1,2,3,4,5,6,7,8,9} #it removes repeated values
print(set1.union(set2)) #{1,2,3,4,5,6,7,8,9}


#6. set.interection(set2) #combines common values & return new
print(set1.intersection(set2)) #{1,2,3,4,5}
#it returns common value

