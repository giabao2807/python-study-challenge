#closure là khai báo hàm trong hàm khác
#khai báo hàm hello trong hàm welcome và trả về hello

def welcome(greeting: 'lời chào'):
	def hello(name: 'tên người'):
		print(f'{greeting},{name}. Welcome to my chanel')
	return hello

hi = welcome('Hello')
hi('Anh Khoa')