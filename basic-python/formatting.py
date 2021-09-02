name ="Giabao"
age = 20
print("%s is %d years old" %(name,age))

#object is not string can use %d
mylist = [1,2,3]
print("A list: %s" %mylist)

#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#%f - Floating point numbers
#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#%x/%X - Integers in hex representation (lowercase/uppercase)

#exercise
data=("John","Doe",53.44)
format_string="hello %s %s. Your current balance is $%s"
print (format_string %data)