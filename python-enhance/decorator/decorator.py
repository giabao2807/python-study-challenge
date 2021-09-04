def display_decorator(func):
	def wrapper(str):
		#logic trước khi chạy hàm func
		print(f'Log: the function {func.__name__} is executing...')
		func(str)
		#logic sau khi chạy hàm func
		print(f'Log: Execution completed.\n')
	return wrapper

def display(str):
	print(str)

display = display_decorator(display)
display('hello gia bảo')

@display_decorator
def say_hello(str):
	print(str)

say_hello('Hello anh khoa')