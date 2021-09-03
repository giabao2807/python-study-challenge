x=2
print(x==2)
print(x==3)

name ="Gia Bao"
age=20
if name == "Gia Bao" and age ==20:
	print("Your name is Gia Bao, and you are also 20 years old")

if name=="Gia Bao" or name == "Anh khoa":
	print("Name is Bao or Khoa") 


#in
if name in ["Gia Bao","Anh Khoa"]:
	print("Name is Bao or Khoa")

#if and else if
statement = False
another_statement = True
if statement is True :
	print("statement")
	pass
elif another_statement is True : #else if
	print("another_statement")
	pass
else :
	print("no statement is correct")
	pass

#operator is
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

#operator not
print(not False) # Prints out True
print((not False) == (False)) # Prints out False


#Excersise
print("Exercise: change value to true")
number = 16
second_number =0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")








