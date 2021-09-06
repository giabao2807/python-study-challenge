def fibo(count:int=15):
	a,b=0,1
	i=0
	while True:
		if i>count:
			break
		yield a
		a,b =b,a+b
		i+=1

def yield_return():
	i=0
	yield i+10
	yield i*10
	yield i/10
	yield i-10

def test1():
 	iterable = fibo(15)
 	for f in iterable:
 		print(f, end=' ')
 	print()

def test2():
	for value in yield_return():
		print(value)


if __name__ == '__main__':
	test1()
	test2()
	#là một biểu thức generator -> trả về là biến squares trỏ tới.
	#biến squares là iterator
	squares =(x*x for x in range(1,20,2))
	for s in squares:
		print(s, end= ' ')
