class decoclass(object):
	def __init__(seft,f):
		seft.f = f

	def __call__(seft,*args,**kwargs):
		#logic trước khi gọi hàm f
		print('decorator initialised')
		seft.f(*args,**kwargs)
		print('decorator deminated')
		#logic sau khi gọi hàm f


@decoclass
def hello(name):
	print(f'Hello,{name}. Welcome to my chanel')

hello('Gia Bảo')