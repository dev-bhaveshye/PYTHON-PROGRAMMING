marks = {
"bhavesh":100,
"yash":150

}
print(marks , type(marks))

marks.update({"bhavesh":99, "yash":57}) # updation
print(marks)

print(marks.items()) # prints items in a dictionary

print(marks.keys()) #prints keys in a dictionary

print(marks.get("bhavesh")) #it use to written a value of key

#print(marks.get("bhavesh2")) / if it is not present in the dictionary it will return none 

#print(marks["bhavesh2"]) /  if it is not present in the dictionary it will return ERROR 

marks.pop("bhavesh") #used to remove a specified key and return the corresponding value.
print(marks)

marks.popitem() #method returns and removes the last key-value pair from the dictionary.
print(marks)