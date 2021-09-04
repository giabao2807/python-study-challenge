def hello (name):
	print(f'Hello,{name}. Wellcome to heaven!' )

def hi(name):
	print(f'hi, {name}. Welcome to my chanel!')


#hàm bậc cao: nhận tham số là một hàm khác
def greeting(name,func):
	print('Inside high order function: ')
	func(name)
	print('--------------')

greeting('Gia Bảo', hello)
greeting('Anh Khoa',hi)