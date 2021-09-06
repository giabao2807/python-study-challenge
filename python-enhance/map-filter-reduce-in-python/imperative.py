'''Tạo ra danh sách y tính theo y=ax+b với x trong list dưới'''
X=[x/100 for x in range(100,1000)]

Y=[]

def perform(x,a=1.0,b=2.0):
	return a*x + b 

for x in X:
	y=perform(x)
	Y.append(y)

for y in Y:
	print(y, end= ' ')