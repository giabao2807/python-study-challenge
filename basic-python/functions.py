def my_function():
	print("Hello form my function")

def my_function_with_args(username, age):
	print("Hello my name is %s I'm %d years olds" %(username,age))

def sum(a,b):
	return a+b

my_function()

my_function_with_args("giabao",20)

print(sum(3,4))

#exercise
# Modify this function to return a list of strings as defined above
def list_benefits():
	return["a","b","c"]


# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
	return benefit + " is a benefit of functions!"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()