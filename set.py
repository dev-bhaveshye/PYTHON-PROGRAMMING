# elements in set does not repeat,  it return the element once
#elemnts are unordered but not repeated 
s= {1, 2, 3, "bahvesh"}
type(s)

#to create a empty set use s=set() , dont use s={}because it will be a dict
z=set()
print(type(z))

#add element in set 
s.add(25)
print(s)

#remove element
s.remove(1)
print(s)