from functools import reduce

def fun_fact(n:int):
	return reduce(lambda x,y:x*y,range(1,n+1))


if __name__ == '__main__':
	n=3
	print(fun_fact(3))

#cú pháp lambda: lambda <dsach tham so> : bieu thc ket qua
'''
	lambda x, y: x *y
	lambda p : True if p.age >= 75 else False
	lambda x, a=1.0, b=0.0, c=0.0: a * x * x + b * x + c
'''