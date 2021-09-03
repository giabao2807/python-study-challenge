phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

phonebook1 = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook1)

print("==============loops in dictionaries=========")
#loops
for name, number in phonebook1.items() :
	print("Phone number of %s is %d" %(name,number))


print("==========Del a value===========")
#remove a value
del phonebook["John"]
print(phonebook)

phonebook.pop("Jack")
print(phonebook)


#exercise 
phonebookex = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
# your code goes here
phonebookex["Jake"] =28072001
del phonebookex["Jill"]

# testing code
if "Jake" in phonebookex:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebookex:      
    print("Jill is not listed in the phonebook.") 