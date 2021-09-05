def foo(**kwargs):
	for key,value  in kwargs.items():
		print(f'{key} = {value}')


foo(a=2,b=2,c=3)


print("============another example==========")
def sum( start:int, **numbers):
	for _,value in numbers.items():
		start+= value
	return start


print(sum(start=0, a=1,b=2))